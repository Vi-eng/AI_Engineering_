# pdf_agent.py
import os
import uuid
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
import pdfplumber
from typing import List, Dict

load_dotenv()

# === CONFIG ===
MAX_HISTORY = 12
SESSION_DIR = "sessions"
TOOLS = []  # add other custom tools if needed

if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)

# === LLM ===
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# === AGENT ===
agent_executor = create_react_agent(llm, TOOLS)

# === SESSION MEMORY ===
sessions = {}


def get_session_path(session_id: str) -> str:
    return os.path.join(SESSION_DIR, f"{session_id}.json")


def load_session(session_id: str) -> List[Dict]:
    if session_id in sessions:
        return sessions[session_id]

    path = get_session_path(session_id)
    if os.path.exists(path):
        with open(path, "r") as f:
            sessions[session_id] = json.load(f)
    else:
        sessions[session_id] = []

    return sessions[session_id]


def save_session(session_id: str):
    path = get_session_path(session_id)
    with open(path, "w") as f:
        json.dump(sessions[session_id], f, indent=2)


def add_message(session_id: str, role: str, content: str):
    sessions[session_id].append({"role": role, "content": content})


# === PDF / TEXT PROCESSING ===
def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def summarize_document(text: str) -> str:
    """
    Generates a concise structured summary using Groq.
    """
    response = agent_executor.invoke({
        "messages": [{"role": "user", "content": f"Summarize the following document into structured insights:\n\n{text}"}]
    })
    return response["messages"][-1].content


# === MAIN ROUTER ===
def run_agent(user_input: str, session_id: str = None, pdf_path: str = None) -> dict:
    try:
        # Create or load session
        if not session_id:
            session_id = str(uuid.uuid4())

        history = load_session(session_id)

        # Process PDF if provided
        if pdf_path:
            doc_text = extract_text_from_pdf(pdf_path)
            user_input = f"Analyze the following document and extract structured insights:\n\n{doc_text}"

        # Add user message
        add_message(session_id, "user", user_input)

        # Trim history
        trimmed_history = history[-MAX_HISTORY:]

        # Call LangGraph agent
        response = agent_executor.invoke({"messages": trimmed_history})
        bot_reply = response["messages"][-1].content

        # Save assistant message
        add_message(session_id, "assistant", bot_reply)

        # Persist session
        save_session(session_id)

        return {
            "session_id": session_id,
            "response": bot_reply,
            "history_length": len(sessions[session_id])
        }

    except Exception as e:
        return {"session_id": session_id, "response": f"⚠️ Error: {str(e)}"}


# === SAMPLE DOCUMENTS ===
if __name__ == "__main__":
    # Example 1: plain text
    sample_text = """
    Victory Osazuwa-Ojo submitted a use case analysis for AI adoption in LAPO Microfinance Bank.
    Key areas include credit scoring automation, customer support chatbots, and predictive loan approvals.
    """
    result = run_agent(sample_text)
    print("Plain text summary:\n", result["response"])

    # Example 2: PDF
    pdf_file = "THE ESSENTIAL GUIDE TO FILMMAKING.pdf"
    if os.path.exists(pdf_file):
        pdf_result = run_agent(user_input="", pdf_path=pdf_file)
        print("PDF summary:\n", pdf_result["response"])