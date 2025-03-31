import json
import os
from typing import Any, Dict
import requests

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/api/retrieve")
def retrieve(state: str, fuel: str, sector: str, tone: str = "professionally"):
    # In a full web app we would hold the api key in secrets or an environment variable. For the sake of simplicity, I'm hard coding for now
    eia_url = "https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data?api_key=d4eTbnwrwg3T8Dzlw1pP2ErvZAlTjqrrjaWdNskc"

    eia_params = {
        "frequency": "annual",
        "data": ["value"],
        "facets": {
            "stateId": [state], 
            "fuelId": [fuel],
            "sectorId": [sector]
        },
        "start": "1970",
        "end": "2022",
        "sort": [
            {
                "column": "period",
                "direction": "desc"
            }
        ],
        "offset": 0,
        "length": 5000
    }

    eia_headers = {
        "X-Params": json.dumps(eia_params)
    }

    try:
        eia_result = perform_get_request(url=eia_url, headers=eia_headers)
        
        data = eia_result.get("response", {}).get("data")
        if not data:
            message = f"No data in response from EIA. eia_result: {eia_result}"
            print(message)
            return {"message": message}
    
    except Exception as e:
        message = f"Unknown exception when sending a request to EIA. Error: {e}"
        print(message)
        return {"message": message}

    return {"message": "a successful retrieval", "data": data}