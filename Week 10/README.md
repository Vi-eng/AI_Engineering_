---

# PDF/Text Groq Agent

A Python AI agent that reads **PDF files or plain text**, processes them with **Groq LLM**, and extracts **structured insights**. It supports session memory to track conversations and can generate concise summaries for reports, dashboards, or analytics.

---

## Features

* Extract text from PDF files using `pdfplumber`.
* Summarize plain text or PDF content into structured insights using **ChatGroq**.
* Maintain per-session memory in JSON files to preserve conversation history.
* Handle multi-turn interactions with a **history limit** to avoid token overflow.
* Easily extensible with additional LangGraph tools.

---

## Requirements

* Python 3.11+
* Packages:

  ```bash
  pip install python-dotenv langchain-groq langgraph pdfplumber
  ```

---

## Configuration

1. Create a `.env` file in the root directory for your API keys:

   ```env
   GROQ_API_KEY=<your_groq_api_key>
   ```
2. Ensure a `sessions/` directory exists (the script will auto-create if missing).

---

## Usage

### 1. Run on plain text

```python
from pdf_agent import run_agent

text = """
Victory Osazuwa-Ojo submitted a use case analysis for AI adoption in LAPO Microfinance Bank.
Key areas include credit scoring automation, customer support chatbots, and predictive loan approvals.
"""
result = run_agent(text)
print("Summary:\n", result["response"])
```

### 2. Run on a PDF file

```python
pdf_file = "sample_report.pdf"
result = run_agent(user_input="", pdf_path=pdf_file)
print("PDF Summary:\n", result["response"])
```

---

## How It Works (Architecture)

1. **Input Detection**: Determines if input is PDF or plain text.
2. **Text Extraction**: Uses `pdfplumber` to read PDF content.
3. **Text Preprocessing**: Formats the content for the LLM.
4. **Groq LLM Processing**: Generates structured insights.
5. **Session Memory**: Stores user + assistant messages in JSON.
6. **Output**: Returns structured summary to the user.

*See `pdf_agent.py` for full implementation.*

---

## Session Management

* Sessions are stored in `sessions/{session_id}.json`.
* Each session retains a **maximum of 12 messages** (configurable via `MAX_HISTORY`).
* New sessions are automatically created if `session_id` is not provided.

---

## Extensibility

* You can add custom **tools** to `TOOLS` (e.g., currency, weather, analytics) and the agent will invoke them when needed.
* The structured insights can be modified to output **JSON, tables, or key-value pairs** for easier integration.

---

## Example Output

**Input (PDF or Text):**

```
Victory Osazuwa-Ojo submitted a use case analysis for AI adoption in LAPO Microfinance Bank.
Key areas include credit scoring automation, customer support chatbots, and predictive loan approvals.
```

**Output (Structured Insights):**

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

* For PDFs with complex layouts or scanned images, consider integrating **OCR fallback** (e.g., `pytesseract` + `pdf2image`).
* Keep your **Groq API key** secure in `.env`.
* Session files may grow over time; consider periodic cleanup.

---

