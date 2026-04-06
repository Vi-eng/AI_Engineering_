# AI Engineering Bootcamp - Week 7

## 🧠 Stateful AI Agent (With Session Memory)

This project implements a **stateful AI agent** using LangGraph and Groq.
Unlike stateless chatbots, this agent **remembers past interactions within a session and across restarts**.

---

## 🚀 Features

* ✅ Tool-calling agent (weather, currency, etc.)
* ✅ **Session-based memory (stateful conversations)**
* ✅ Persistent storage using JSON files
* ✅ Resume conversations using session IDs
* ✅ Context-aware responses across multiple turns

---

## ⚙️ Prerequisites

* Python 3.11 installed

---

## 🛠️ Setup

1. (Optional but recommended) Create and activate a virtual environment:

   **Windows PowerShell:**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   **Windows Command Prompt:**

   ```cmd
   python -m venv venv
   venv\Scripts\activate.bat
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Application

```bash
python main.py
```

---

## 💬 How Stateful Memory Works

Each conversation is assigned a **unique session ID**.

* Messages are stored in:

  ```
  sessions/<session_id>.json
  ```
* The agent:

  1. Loads previous messages
  2. Sends them to the LLM as context
  3. Saves new messages after each interaction

---

## 🔁 Example Usage

### First Interaction

```text
You: My name is Victory
Bot: Nice to meet you, Victory!
```

### Follow-up (Same Session)

```text
You: What is my name?
Bot: Your name is Victory.
```

---

## 🔄 Resuming a Previous Session

You can continue a past conversation using:

```text
/load <session_id>
```

Example:

```text
/load abc123
```

The agent will reload previous messages and continue the conversation.

---

## 📁 Project Structure

```
project/
│
├── main.py        # Terminal interface
├── agent.py       # Stateful agent logic
├── tools.py       # Tool functions (weather, currency, etc.)
├── sessions/      # Stored conversation history (auto-created)
└── .env           # API keys (Groq, etc.)
```

---

## 🧠 Memory Management

To prevent excessive memory usage:

* Only the **most recent messages** are sent to the LLM
* Older messages remain stored but are trimmed during inference

---

## ⚡ Notes

* Using a virtual environment is recommended
* Session files persist even after closing the application
* You can modify tools or extend memory logic as needed

---

## 🚀 Future Improvements

* Replace JSON storage with Redis (for scalability)
* Add long-term memory (vector database / FAISS)
* Implement automatic user profile extraction
* Integrate with FastAPI or Rasa for production deployment

---

