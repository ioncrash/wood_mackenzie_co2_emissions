import boto3
import json

# 1. Setup Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

# 2. Define your variable values
table = [
        {
            "period": "2022",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "4.351594",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2021",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "4.205504",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2020",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "2.916224",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2019",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "4.64467",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2018",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "4.985783",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2017",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "4.976193",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2016",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "3.617266",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2015",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "5.694773",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2014",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "5.851337",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2013",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "6.284246",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2012",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "5.550496",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2011",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "6.187755",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2010",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "6.231363",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2009",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "4.391469",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2008",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "7.729247",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2007",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "7.078892",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2006",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "7.487914",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2005",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "7.216799",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2004",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "7.256594",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2003",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "6.918884",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2002",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "6.758777",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2001",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "9.23054",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "2000",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "9.776159",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1999",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "11.171841",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1998",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "9.152593",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1997",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "8.889966",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1996",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "10.055741",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1995",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "10.22189",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1994",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "10.024845",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1993",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "7.388854",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1992",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "7.234124",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1991",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "8.732252",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1990",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "11.088307",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1989",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "11.189314",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1988",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "12.303901",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1987",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "11.627129",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1986",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "16.009356",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1985",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "15.818079",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1984",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "15.73309",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1983",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "15.663568",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1982",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "17.114605",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1981",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "18.870375",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1980",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "20.344015",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1979",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "19.412676",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1978",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "15.600595",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1977",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "17.487238",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1976",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "20.85877",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1975",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "22.84113",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1974",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "19.536747",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1973",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "26.256741",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1972",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "30.821728",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1971",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "29.862873",
            "value-units": "million metric tons of CO2"
        },
        {
            "period": "1970",
            "sectorId": "IC",
            "sector-name": "Industrial carbon dioxide emissions",
            "fuelId": "CO",
            "fuel-name": "Coal",
            "stateId": "MI",
            "state-name": "Michigan",
            "value": "29.880584",
            "value-units": "million metric tons of CO2"
        }
    ]


state = "IL"
fuel = "coal"
sector = "industrial"
tone = "professional"

# 3. Template as string
prompt = f"""
This is a table of data containing CO2 emissions in the state of {state} for the fuel {fuel} in the {sector} sector. Summarize any trends you see as a bullet pointed list, making note of any peaks, valleys, or anomalies. There may be more than one of each. Format the list with an empty line between each bullet point. 

Include a section about each decade and broad changes that occured within that decade.

Do this {tone}

There's no need to comment that there are many possible factors behind these fluctuations, or to comment that further analysis and context are required. Just the summary, please.

{table}
"""

# 5. Construct the request body
body = {
    "messages": [
        {
            "role": "user",
            "content": prompt.strip()
        }
    ],
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 500,
    "temperature": 0.7
}

# 6. Call invoke_model
response = bedrock.invoke_model(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    contentType="application/json",
    accept="application/json",
    body=json.dumps(body)
)

# 7. Parse and print response
response_body = json.loads(response["body"].read())
print("\nClaude Response:\n")
print(response_body["content"][0]["text"])
