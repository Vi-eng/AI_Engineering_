from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Inquiry(BaseModel):
    question: str
    # category: str  # e.g. "absence", "fees", "complaint"

def build_prompt(question):
    return f"""
You are Wendy, a professional school administrator.

Write a polite, clear, and professional response to the Parent/Guardian's inquiry. If you don't know the answer, say "Please contact the school office for more details.":

User Query:
{question}

Response:
"""

@app.post("/ask")
def generate_response(data: Inquiry):
    prompt = build_prompt(data.question)

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful school administrator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )

    return {
        "answer": completion.choices[0].message.content
    }