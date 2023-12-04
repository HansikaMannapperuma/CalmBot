import openai

def analyze_gpt35(text):
    messages = [
        {"role": "system", "content": """You are trained to analyze and detect the sentiment of given text.
        determine if the sentiment is: positive,negative or neutral. Return answer in single word as either positive or negative 
                                        If you're unsure of an answer, you can say "neutral" """},
        {"role": "user", "content": text}
        ]

    response = openai.ChatCompletion.create(
                      model="gpt-3.5-turbo",
                      messages=messages,
                      max_tokens=1,
                      n=1,
                      stop=None,
                      temperature=0)

    response_text = response.choices[0].message.content.strip().lower()

    return response_text
