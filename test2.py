import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                                          {"role": "user", "content": "give me one tip on nutrition management "}])
print(completion.choices[0].message.content)
