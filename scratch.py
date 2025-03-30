import boto3
import json

# 1. Setup Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

# 2. Define your variable values
table = """
Year | Emissions (MMT CO2)
2008 | 7.2
2009 | 9.5
2010 | 7.4
2011 | 8.9
2012 | 10.1
2013 | 10.4
2014 | 9.8
2015 | 9.0
2016 | 8.1
2017 | 7.6
2018 | 7.3
2019 | 7.0
2020 | 6.5
2021 | 6.8
2022 | 6.4
"""


state = "IL"
fuel = "coal"
sector = "industrial"
tone = "professional"

# 3. Template as string
prompt = f"""
This is a table of data containing CO2 emissions in the state of {state} for the fuel {fuel} in the {sector} sector. Summarize any trends you see as a bullet pointed list, making note of any peaks, valleys, or anomalies. There may be more than one of each. Format the list with an empty line between each bullet point. Do this {tone}

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
