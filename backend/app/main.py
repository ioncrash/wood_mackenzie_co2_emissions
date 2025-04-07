import json
import os
from typing import Any, Dict, List, Optional

import boto3
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
EIA_API_KEY = os.getenv("EIA_API_KEY")
AWS_REGION = os.getenv("AWS_REGION")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def perform_get_request(url: str, headers: Dict[str, Any]):
    try:
        response = requests.get(url, headers=headers)
        if not response.ok:
            message = f"Request to {url} with headers {headers} was unsuccessful. Error {response.status_code}: {response.text}"
            print(message)
            raise Exception(message)

        return json.loads(response.text)

    except Exception as e:
        message = f"Exception when sending a request to {url} with headers {headers}. Error: {e}"
        print(message)
        raise Exception(message)


def request_eia_data(state: str, fuel: str, sector: str):
    eia_url = f"https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data?api_key={EIA_API_KEY}"

    eia_params = {
        "frequency": "annual",
        "data": ["value"],
        "facets": {"stateId": [state], "fuelId": [fuel], "sectorId": [sector]},
        "start": "1970",
        "end": "2022",
        "sort": [{"column": "period", "direction": "desc"}],
        "offset": 0,
        "length": 5000,
    }

    eia_headers = {"X-Params": json.dumps(eia_params)}

    return perform_get_request(url=eia_url, headers=eia_headers)


def construct_claude_prompt(
    state: str, fuel: str, sector: str, data: List[Dict[str, Any]], tone: str
):
    fuel_lookup = {
        "CO": "coal",
        "NG": "natural gas",
        "PE": "petroleum",
        "TO": "all fuel",
    }

    fuel_str = fuel_lookup[fuel]

    sector_lookup = {
        "CC": "commercial",
        "IC": "industrial",
        "TC": "transportation",
        "EC": "electric power",
        "RC": "residential",
    }

    sector_str = sector_lookup[sector]

    return f"""
        This is a set of data containing CO2 emissions in the state of {state} for the {fuel_str} in the {sector_str} sector. 
        
        {data}
        
        Summarize any overall trends you see, making note of any peaks, valleys, or anomalies. There may be more than one of each. 

        Also include a section about each decade and broad changes that occured within that decade. Put an newline between each decade.

        If I have already sent a different set of data, include a section calling out any direct or indirect correlations between this and the coal data I sent previously, if there are any. Be specific about the years those correlations are most obvious

        Do this {tone or "professionally"}

        There's no need to comment that there are many possible factors behind these fluctuations, or to comment that further analysis and context are required. Just the summary, please.
    """


def perform_claude_request(
    state: str,
    fuel: str,
    sector: str,
    tone: str,
    data: List[Dict[str, Any]],
    messages: List[Dict[str, str]] = [],
):
    bedrock = boto3.client("bedrock-runtime", region_name=AWS_REGION)

    prompt = construct_claude_prompt(
        state=state, fuel=fuel, sector=sector, data=data, tone=tone
    )

    messages.append({"role": "user", "content": prompt.strip()})

    body = {
        "messages": messages,
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1500,
        "temperature": 0.7,
    }

    claude_response = bedrock.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body),
    )

    claude_response_body = json.loads(claude_response["body"].read())

    if (
        not claude_response_body["content"]
        or not claude_response_body["content"][0]["text"]
    ):
        message = f"No text in response from Claude. claude_response_body: {claude_response_body}"
        print(message)
        raise Exception(message)

    response_text = claude_response_body["content"][0]["text"]

    messages.append({"role": "assistant", "content": response_text})

    return messages


@app.get("/api/retrieve")
def retrieve(
    state: str = Query(...),
    fuel: str = Query(...),
    sector: str = Query(...),
    tone: Optional[str] = Query("professionally"),
    messages: Optional[str] = Query("[]"),
):
    # Parse messages safely
    try:
        past_messages = json.loads(messages)
    except json.JSONDecodeError:
        print(f"Malformed JSON in 'messages': {messages}")
        raise HTTPException(status_code=400, detail="Malformed 'messages' parameter")

    # Get EIA data
    try:
        eia_result = request_eia_data(state=state, fuel=fuel, sector=sector)
        data = eia_result.get("response", {}).get("data", [])
        if not data:
            raise HTTPException(
                status_code=404, detail="No data found for given parameters"
            )
    except Exception as e:
        print(f"EIA request failed: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch EIA data: {e}")

    # Call Claude
    try:
        conversation = perform_claude_request(
            state=state,
            fuel=fuel,
            sector=sector,
            tone=tone,
            data=data,
            messages=past_messages,
        )
    except Exception as e:
        print(f"Claude request failed: {e}")
        raise HTTPException(status_code=500, detail=f"Claude request error: {e}")

    return {"message": "", "data": data, "conversation": conversation}
