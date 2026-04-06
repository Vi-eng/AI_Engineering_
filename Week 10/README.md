
---

# PDF/Text Groq Agent with REST API & Web UI

A Python AI agent that reads **PDF files or plain text**, processes them with **Groq LLM**, and extracts **structured insights**.
This version adds a **REST API** and a **local web UI**, enabling interactive querying of text and PDF documents, with session memory support for multi-turn conversations.

---

## Features

* Extract text from **PDF files** using `pdfplumber`.
* Summarize **plain text** or **PDF content** into structured insights via **ChatGroq**.
* REST API endpoint (`/chat`) that accepts text or PDF and returns **JSON** responses.
* Local **web UI** for submitting text or PDF files and viewing structured insights.
* Maintain **per-session memory** in JSON files to preserve conversation history.
* Handle multi-turn interactions with a **history limit** to avoid token overflow.
* Easily extensible with additional **LangGraph tools** (e.g., weather, currency, analytics).

---

## Requirements

* Python 3.11+
* Packages:

```bash
pip install python-dotenv langchain-groq langgraph pdfplumber fastapi uvicorn
```

---

## Configuration

1. Create a `.env` file in the root directory for your API keys:

```env
GROQ_API_KEY=<your_groq_api_key>
```

2. Ensure a `sessions/` directory exists (the script auto-creates if missing).

---

## Running the REST API Locally

1. Start the API server:

```bash
python api.py
```

2. Endpoints:

| Path       | Method | Description                                            |
| ---------- | ------ | ------------------------------------------------------ |
| `/chat`    | POST   | Send text or PDF to the agent, returns JSON.           |
| `/health`  | GET    | Health check, returns `{"status": "ok"}`               |
| `/static/` | GET    | Serves web UI (`index.html`, `style.css`, `script.js`) |

---

## Web UI

* Access the UI at: `http://127.0.0.1:8000/`
* Features:

  * Text area to submit plain text.
  * File upload for PDFs.
  * Displays agent JSON response interactively.

---

## Usage Examples

### 1. Plain Text

```python
from pdf_agent import run_agent

text = """
Victory Osazuwa-Ojo submitted a use case analysis for AI adoption in LAPO Microfinance Bank.
Key areas include credit scoring automation, customer support chatbots, and predictive loan approvals.
"""
result = run_agent(text)
print("Summary:\n", result["response"])
```

### 2. PDF File

```python
pdf_file = "sample_report.pdf"
result = run_agent(user_input="", pdf_path=pdf_file)
print("PDF Summary:\n", result["response"])
```

### 3. Using the API (cURL)

```bash
# Text input
curl -X POST "http://127.0.0.1:8000/chat" -F "user_input=Summarize this document"

# PDF input
curl -X POST "http://127.0.0.1:8000/chat" -F "pdf_file=@sample_report.pdf"
```

---

## How It Works (Architecture)

1. **Input Detection**: Detects PDF or plain text input.
2. **Text Extraction**: Uses `pdfplumber` to read PDFs.
3. **Text Preprocessing**: Formats content for the LLM.
4. **Groq LLM Processing**: Generates structured insights.
5. **Session Memory**: Stores user + assistant messages in `sessions/{session_id}.json`.
6. **Output**: Returns structured summary via Python, API, or Web UI.

**Workflow Diagram:**

```
+------------------+
|  User Input      |
| (Text or PDF)    |
+--------+---------+
         |
         v
+--------+---------+
| Text Extraction  |
|  (pdfplumber)    |
+--------+---------+
         |
         v
+--------+---------+
| Preprocessing    |
+--------+---------+
         |
         v
+--------+---------+
| Groq LLM Agent   |
| (ChatGroq + Tools)|
+--------+---------+
         |
         v
+--------+---------+
| Session Memory   |
| (JSON per session)|
+--------+---------+
         |
         v
+------------------+
| Output (JSON /   |
| Structured Data) |
+------------------+
```

---

## Session Management

* Sessions are stored in `sessions/{session_id}.json`.
* Maximum of 12 messages per session (configurable via `MAX_HISTORY`).
* New sessions are automatically created if `session_id` is not provided.

---

## Extensibility

* Add custom **tools** to `TOOLS` in `pdf_agent.py` (e.g., currency, weather, analytics).
* Configure structured insights output as **JSON, tables, or key-value pairs** for easier integration.

---

## Example Structured Output

**Input (Text or PDF):**

```
Victory Osazuwa-Ojo submitted a use case analysis for AI adoption in LAPO Microfinance Bank.
Key areas include credit scoring automation, customer support chatbots, and predictive loan approvals.
```

**Output (Structured JSON):**

```json
{
  "author": "Victory Osazuwa-Ojo",
  "organization": "LAPO Microfinance Bank",
  "key_areas": [
    "Credit scoring automation",
    "Customer support chatbots",
    "Predictive loan approvals"
  ]
}
```

---

## Notes

* PDFs with complex layouts or scanned images may require **OCR fallback** (`pytesseract` + `pdf2image`).
* Keep your **Groq API key** secure in `.env`.
* Session files may grow over time; consider periodic cleanup.
* The UI and API are local by default; adjust CORS and endpoints for production deployment.

---
