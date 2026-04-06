# agent.py
from tools import weather_tool, currency_tool
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import uuid
import json
import os

load_dotenv()

# === CONFIG ===
MAX_HISTORY = 12
SESSION_DIR = "sessions"

if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)

TOOLS = [weather_tool, currency_tool]

# === LLM ===
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# === AGENT ===
agent_executor = create_react_agent(llm, TOOLS)

# === SESSION MEMORY ===
sessions = {}


def get_session_path(session_id: str):
    return os.path.join(SESSION_DIR, f"{session_id}.json")


def load_session(session_id: str):
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
    sessions[session_id].append({
        "role": role,
        "content": content
    })


# === MAIN ROUTER ===
def run_agent(user_input: str, session_id: str = None) -> dict:
    try:
        # Create or load session
        if not session_id:
            session_id = str(uuid.uuid4())

        history = load_session(session_id)

        # Add user message
        add_message(session_id, "user", user_input)

        # Trim history (avoid token overflow)
        trimmed_history = history[-MAX_HISTORY:]

        # Call LangGraph agent
        response = agent_executor.invoke({
            "messages": trimmed_history
        })

        # Extract final response
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
        return {
            "session_id": session_id,
            "response": f"⚠️ Error: {str(e)}"
        }