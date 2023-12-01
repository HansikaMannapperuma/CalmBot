import asyncio

from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from gptapi_module import generate_openai_response

app = FastAPI()
messages = []


async def generate_response_async(messages, immediate_response):
    try:
        response = await generate_openai_response(messages)
        # Notify Dialogflow that the response is ready (You may need to implement this part)
        # For simplicity, let's assume a hypothetical function notify_dialogflow
        print(messages)
        print(f"GPT Response: {response}")
        notify_dialogflow(response)
    except Exception as e:
        # Handle errors during asynchronous processing
        print(f"Error during async processing: {str(e)}")


@app.post('/')
async def webhook(request: Request, background_tasks: BackgroundTasks) -> dict:
    try:
        payload = await request.json()
        intent = payload['queryResult']['intent']['displayName']
        question = payload['queryResult']['queryText']

        if intent == "StressManagementTips":
            messages.append({"role": "user", "content": question})

            # Send immediate response to Dialogflow
            immediate_response = {"fulfillmentText": "I'm working on it. Please wait."}
            background_tasks.add_task(generate_response_async, messages, immediate_response)

            return JSONResponse(content=immediate_response)
    except Exception as e:
        # Handle errors during request processing
        print(f"Error processing request: {str(e)}")
        return JSONResponse(content={'fulfillmentText': 'Something went wrong.'})


# Mock function for generating response asynchronously (Replace this with your GPT API call)
# async def generate_openai_response(messages):
#     # Simulating some asynchronous processing time
#     # await asyncio.sleep(10)
#     return "Your generated response from GPT API"


# Mock function for notifying Dialogflow (Replace this with actual implementation)
def notify_dialogflow(response):
    print(f"Notifying Dialogflow: {response}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
