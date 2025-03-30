import os
import requests
import json

# URL to EIA CO2 Emissions Aggregates endpoint
api_key = os.getenv("EIA_API_KEY")
url = f"https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data?api_key={api_key}"

# Prepare the JSON payload for the custom header
params = {
    "frequency": "annual",
    "data": ["value"],
    "facets": {
        "stateId": ["IL"],     # Illinois
        "fuelId": ["CO"],      # Coal
        "sectorId": ["IC"]     # Industrial
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

# Send the GET request
response = requests.get(url, headers=headers)

# Print status and data
print("Status code:", response.status_code)
print("Response JSON:\n", json.dumps(response.json(), indent=2))
