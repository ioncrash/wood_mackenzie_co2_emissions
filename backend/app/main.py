import json
import os
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


@app.get("/api/retrieve")
def retrieve(state: str, fuel: str, sector: str, tone: str = "professionally"):
    # In a full web app we would hold the api key in secrets or an environment variable. For the sake of simplicity, I'm hard coding for now
    url = "https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data?api_key=d4eTbnwrwg3T8Dzlw1pP2ErvZAlTjqrrjaWdNskc"

    params = {
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

    # Set the custom header
    headers = {
        "X-Params": json.dumps(params)
    }
    try:
        # Send the GET request
        response = requests.get(url, headers=headers)
    except Exception as e:
        message = f"Unknown exception when sending a request to EIA. Error: {e}"
        print(message)
        return {"message": message}

    if not response.ok:
        message = f"Request to EIA was unsuccessful. Error {response.status_code}: {response.text}"
        print(message)
        return {"message": message}
    
    json_response = json.loads(response.text)
    
    data = json_response.get("response", {}).get("data")
    if not data:
        message = f"No data in response from EIA. Full text: {response.text}"
        print(message)
        return {"message": message}

    return {"message": "a successful retrieval", "data": data}