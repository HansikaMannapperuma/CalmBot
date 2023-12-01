from dotenv import load_dotenv
from fastapi import FastAPI, BackgroundTasks
from fastapi import Request
from fastapi.responses import JSONResponse
import os
import openai


load_dotenv()
app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

def generate_openai_response(messages):
    try:
        print("Before OpenAI API call")

        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, timeout=2,
                                       max_tokens=80, temperature=0.7, top_p=0.9,
                                       frequency_penalty=0, presence_penalty=0.6)
        reply=completion.choices[0].message.content
        print(reply)
        print("After OpenAI API call")

        return reply
    except openai.APITimeoutError:
        # Handle timeout error
        return "Sorry, the request timed out. Please try again later."
    except Exception as e:
        # Log other OpenAI errors
        error_message = f"OpenAI API error: {str(e)}"
        print(error_message)
        raise e



@app.post('/')
async def webhook(request: Request,background_tasks: BackgroundTasks) -> dict:
    try:
        payload = await request.json()
        intent = payload['queryResult']['intent']['displayName']
        question = payload['queryResult']['queryText']

        if intent == "StressManagementTips":
            messages.append({"role": "user", "content": question})


            reply=generate_openai_response(messages)
            return JSONResponse(content={"fulfillment":reply})


    except Exception as e:
        error_message = f"Error processing request: {str(e)}"
        print(error_message)
        return JSONResponse(content={'fulfillmentText': 'Something went wrong.'})

