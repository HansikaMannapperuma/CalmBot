# your_gptapi_module.py
import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_openai_response(messages):
    try:
        # Your GPT API call logic here
        # This is just a placeholder, replace it with your actual implementation
        # chat_completion = client.chat.completions.create(messages=messages, model="gpt-3.5-turbo", timeout=2,
        #                                max_tokens=80, temperature=0.7, top_p=0.9,
        #                                frequency_penalty=0, presence_penalty=0.6)

        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, timeout=2,
                                       max_tokens=80, temperature=0.7, top_p=0.9,
                                       frequency_penalty=0, presence_penalty=0.6)
        reply=completion.choices[0].message.content
        print(reply)

        return reply
    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        print(f"OpenAI API error: {str(e)}")
        raise e
