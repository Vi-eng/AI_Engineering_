from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Inquiry(BaseModel):
    message: str
    category: str  # e.g. "absence", "fees", "complaint"

def build_prompt(message, category):
    return f"""
You are a professional school administrator.

Write a polite, clear, and professional response to the following {category} inquiry:

Inquiry:
{message}

Response:
"""

@app.post("/generate-response")
def generate_response(data: Inquiry):
    prompt = build_prompt(data.message, data.category)

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful school administrator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )

    return {
        "response": completion.choices[0].message.content
    }