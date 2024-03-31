from openai import OpenAI
api_key = "<Enter key>"
client = OpenAI(api_key=api_key)
assistant_message = None
def translate(language1, language2, text):
    desiredlanguage = language1
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[
        {"role": "system", "content": f'Translate the following phrase from {language1} to {language2}: {text}.'}, ])
    return response.choices[0].message.content
