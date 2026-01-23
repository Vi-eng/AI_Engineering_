# Text Processor to CSV

This script downloads or reads text data (including **.docx** files), processes it using Natural Language Processing, and exports the results into a structured CSV file.

## Prerequisites

This script requires **Python 3.x**. You will need to install three external packages:

* `requests` (for downloading data)
* `nltk` (for text processing)
* `python-docx` (for reading Word documents)

> **Pro Tip:** Use a **virtual environment (venv)** to keep these installations separate from your other projects.

## Setup & Installation

### 1. (Optional) Create a Virtual Environment

If you want to use a virtual environment, run these commands in your terminal first:

* **Windows:** `python -m venv venv` then `.\venv\Scripts\activate`
* **Mac/Linux:** `python3 -m venv venv` then `source venv/bin/activate`

### 2. Install Libraries

Run the following command to install the necessary dependencies:

```bash
pip install requests nltk python-docx

```

---

## How to Run

1. **Open the project folder** in VS Code.
2. **Open the script file**: `Text_loader_and_cleaner.py`.
3. **Execute the script**:
* **Option A (Global Environment):** Press the **Run (Play)** button in the top right corner of VS Code.
* **Option B (Virtual Environment):** Use the terminal.
* First, ensure you are in the correct directory. Type `pwd` (Print Working Directory) to check. Use `cd` (Change Directory) to navigate if needed.
* Run the script by typing:
* **Windows:** `py Text_loader_and_cleaner.py`
* **Mac/Linux:** `python3 Text_loader_and_cleaner.py`
4. **Follow the prompts** in the terminal to interact with the script.
