from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("OPENAI-API-KEY")
client = OpenAI(api_key=api_key)

def get_llm_response(prompt: str) -> str:
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a licensed therapist advising a mental health counselor."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=300,
    temperature=0.7)
    return response.choices[0].message.content
