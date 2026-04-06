````markdown
# AI Engineering Bootcamp - Week 8

## 📌 Overview

This project builds on the Week 6 agent system by introducing an **evaluation and accuracy testing framework** for chatbot responses.

The system now not only generates answers using an AI agent but also **measures how accurate those answers are** against expected outputs using semantic similarity and optional LLM-based evaluation.

---

## 🚀 Week 8 Deliverables

### ✅ Added Features
- Test case dataset for evaluation
- Automated chatbot response testing
- Semantic similarity scoring using embeddings
- Pass / Fail classification system
- Accuracy summary reporting
- (Optional) LLM-based evaluation for deeper validation

---

## ⚙️ Prerequisites

- Python 3.11
- Required dependencies (see installation below)

---

## 🔧 Setup

1. (Optional but recommended) Create and activate a virtual environment:

### Windows PowerShell
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
````

### Windows Command Prompt

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

---

2. Install dependencies:

```bash
pip install -r requirements.txt
```

> Ensure the following are included:

* sentence-transformers
* pandas

---

## ▶️ Running the Application

To run the main chatbot system:

```bash
python main.py
```

---

## 🧪 Running Evaluation Tests

The evaluation system tests chatbot responses against predefined expected answers.

### Step 1: Define Test Cases

Test cases are structured as:

```python
{
    "id": "TC001",
    "query": "Your question here",
    "expected": "Expected answer here"
}
```

---

### Step 2: Run Evaluation

The evaluation pipeline will:

1. Send queries to the chatbot
2. Capture responses
3. Compare with expected answers
4. Compute similarity scores
5. Classify results (Pass / Partial / Fail)

---

### Step 3: View Results

Outputs include:

* Query
* Expected Answer
* Actual Answer
* Similarity Score
* Result (Pass/Fail)

---

## 📊 Evaluation Metrics

### 1. Semantic Similarity

* Uses `sentence-transformers`
* Cosine similarity scoring

| Score Range | Result  |
| ----------- | ------- |
| ≥ 0.85      | Pass    |
| 0.70 – 0.84 | Partial |
| < 0.70      | Fail    |

---

### 2. (Optional) LLM-Based Evaluation

* Uses the LLM to judge correctness
* Handles paraphrased answers better than strict matching

---

## 📁 File Structure

* `main.py` → Entry point of the application
* `agent.py` → Core chatbot/agent logic
* `tools.py` → Utility/helper functions
* `evaluation.py` → **(New)** Evaluation pipeline logic
* `test_cases.json` / `.csv` → **(New)** Test dataset

---

## 🧠 How It Works

```
User Query → Agent → Response
                        ↓
                Evaluation Module
                        ↓
        Score + Classification + Report
```

---

## 📈 Example Output

| ID    | Query      | Score | Result  |
| ----- | ---------- | ----- | ------- |
| TC001 | Greeting   | 0.92  | Pass    |
| TC002 | Info Query | 0.81  | Partial |
| TC003 | Edge Case  | 0.45  | Fail    |

---

## 💡 Notes

* Evaluation helps identify weak areas in chatbot performance
* Improves reliability and trustworthiness of AI responses
* Can be extended with dashboards or logging systems

---

## 🔮 Future Improvements

* Add real-time evaluation dashboard
* Integrate evaluation into API responses
* Track response latency and confidence
* Auto-generate test cases from documents
* Store evaluation history for model comparison

---

## 🧾 Summary

Week 8 transforms the chatbot from a simple response generator into a **measurable AI system**, enabling continuous improvement through structured evaluation.

---

```


