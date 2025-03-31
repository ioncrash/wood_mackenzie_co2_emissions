import json
import os
from typing import Any, Dict, List

import boto3
import requests
from dotenv import load_dotenv
from fastapi import FastAPI
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
    state: str, fuel: str, sector: str, tone: str, data: List[Dict[str, Any]]
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

        Do this {tone}

        There's no need to comment that there are many possible factors behind these fluctuations, or to comment that further analysis and context are required. Just the summary, please.
    """


def perform_claude_request(
    state: str, fuel: str, sector: str, tone: str, data: List[Dict[str, Any]]
):
    bedrock = boto3.client("bedrock-runtime", region_name=AWS_REGION)

    prompt = construct_claude_prompt(
        state=state, fuel=fuel, sector=sector, tone=tone, data=data
    )

    body = {
        "messages": [{"role": "user", "content": prompt.strip()}],
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "temperature": 0.7,
    }

    return bedrock.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body),
    )


@app.get("/api/retrieve")
def retrieve(state: str, fuel: str, sector: str, tone: str = "professionally"):
    try:
        eia_result = request_eia_data(state=state, fuel=fuel, sector=sector)

        data = eia_result.get("response", {}).get("data")
        if not data:
            message = f"No data in response from EIA. eia_result: {eia_result}"
            print(message)
            return {"message": message, "data": []}
    except Exception as e:
        message = f"Encountered exception when sending a request to EIA. Error: {e}"
        print(message)
        return {"message": message, "data": []}

    try:
        claude_response = perform_claude_request(
            state=state, fuel=fuel, sector=sector, tone=tone, data=data
        )

        claude_response_body = json.loads(claude_response["body"].read())

        if (
            not claude_response_body["content"]
            or not claude_response_body["content"][0]["text"]
        ):
            message = f"No text in response from Claude. claude_response_body: {claude_response_body}"
            print(message)
            return {"message": message, "data": []}

        message = claude_response_body["content"][0]["text"]
    except Exception as e:
        message = f"Encountered exception when sending a request to Claude. Error: {e}"
        print(message)
        return {"message": message, "data": []}

    return {"message": message, "data": data}
