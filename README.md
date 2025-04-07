### Welcome!

This is a simple full-stack application that I designed to summarize historical trends in CO2 emissions by state. 

The architecture is pretty simple.

React front end, 
FastAPI back end, 
AWS Bedrock using Claude, 
EIA API as a data source


# Front end:
A simple interface with dropdowns for state, fuel type, and economic sector (and also a "tone" text box for having a little fun with the AI)
Below that, a table with the data pulled from EIA so that the user can compare it to what Claude says
Then the conversation between the user and the AI. For the sake of this project I've chosen to display the entire prompt as compiled by the back end, as well as Claude's response

## Workflow:
1. Use the dropdowns to choose a state, fuel type, and economic sector. 
    - If you want, you can also enter a tone in the text box such as "like Hank Hill" (optional)
2. Press Submit to send a request to the back end containing state, fuel type, economic sector, tone, and any previous messages
3. When the response comes back, it updates the messages held in state
4. Updates the table with the most recent data returned from EIA
5. Updates the DOM with the full conversation between the user and the AI
6. Use the dropdowns again to change the prompt
7. Press Submit to send a new request containing state, fuel type, economic sector, tone, and any previous messages
3. When the response comes back, it updates the messages held in state
4. Updates the table with the most recent data returned from EIA
5. Updates the DOM with the full conversation between the user and the AI. The new response will include a comparison between the previous data and the new data

## Considerations and improvements for the front end:
If this was a full-fledged app, I would want the interface to be much more polished, ideally with interactive visualizations. I played around with some of the text-to-image capabilities of Bedrock's Foundation Models and found that none of them generated anything even close to a readable graph out of the box. It was kind of hilarious, but not useful. Since the point was to work with Generative AI and not an existing visualization library, I decided to abandon this idea for now and focus on data.

The table at the top currently only shows the most recent data returned from the back end. This could be a little confusing since I'm also displaying the full conversation, but I didn't want to overcomplicate the presentation since the point is the AI interactions.

It could use more than a little aesthetic pizzazz as well. It's pretty ugly.


# Back end:
A simple FastAPI back end with just one endpoint

## Workflow
1. When the request is received, it starts by retrieving historical data from EIA's API
2. It then populates a prompt template
3. It submits the prompt to Claude via AWS Bedrock, along with all the past conversation between the user and Claude. This allows Claude to compare new data to old data
3. Claude's response gets returned to the front end to be displayed

## Considerations and improvements for the back end:
As it stands, the app is pretty slow. There are a few things we could do about that:

- Give the user more control over the time period they want to analyze. Right now it always looks at all the historical data that's available. Since there isn't a ton of data in the first place, that seemed to me like a more interesting option than limiting it to a few years. As it turns out, though, it takes Claude a long time to analyze 50 years of data.
- Store the CO2 emission data somewhere rather than pinging EIA every time. Since it's historical data, it will never change anyway, so we might as well just have it in a DB or some other storage.
- Store the conversation somewhere rather than passing it across HTTP requests. It's pretty clunky to pass this much data back and forth. In a production app, you would want to store a user id and cache the previous conversation that way so that you don't need such bulky http requests. This would also allow users to retrieve previous conversation if they start a new browser session (if you wanted to do that)


# Considerations and improvements for the app in general

I can't say for sure that Claude is really the best tool for performing complex analysis on large datasets. For this app, it seems to be doing just fine at giving general takeaways from limited data, but for really precise analysis, there are existing data science tools and techniques that might be better suited for the job. If acccuracy was important, I would want to preprocess the data by running it through some of those tools, then using Claude to summarize those insights, rather than having Claude do everything itself.

One of the great advantages of AI and Claude in particular is its ability to use wide historical context to suggest correlations or interpretations of the data. It would be interesting to take an app like this and ask Claude to offer explanations of why changes occured at the times they did. This will make the output more succeptable to hallucination, but it would also offer interesting commentary that might be useful for a human reader.

The app is lacking in some of the guardrails I would expect for a full-stack app, such as handling invalid input on both the front and back ends and gracefully handling some kinds of errors. 

Unit and integration tests would be useful, especially on the front end

Sensitive data like API keys should be stored somewhere safe, such as a key vault


# How to run it:

You will need:

- Python 3.8+
- Node.js + npm (v18+ recommended)
- AWS credentials with Bedrock access
- An active EIA API key

## Running the back end
Create a .env file in the directory backend/app/

It should have these contents

EIA_API_KEY=[your_eia_api_key_here]  
AWS_REGION=[your_aws_region]


Run these commands on the cli

aws configure  
    - follow the prompts to set up your credentials if you haven't already  
cd backend  
pip install -r requirements.txt  
cd app  
uvicorn main:app --reload  

This should spin up your back-end server

## Running the front end
Run these commands 

cd frontend/woods-mackenzie-frontend  
npm install  
npm start

There should now be a front-end server running. You can now visit http://localhost:3000/ in your browser

I also left the readme that came with the React scaffold I'm using, which has more info on the frontend server