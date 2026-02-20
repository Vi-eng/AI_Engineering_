**Data Loading & Cleaning Pipeline (Pandas + NumPy)**

## 📌 Overview

This notebook implements a structured data ingestion and cleaning workflow using **Pandas** and **NumPy**.

It focuses on:

* Loading raw datasets
* Cleaning and standardizing column names
* Safely converting data types
* Preparing structured data for analysis or downstream ML pipelines

This notebook is ideal as a **data preprocessing foundation** for analytics or machine learning workflows.

---

## 🛠 Features

* Modular data loading via `load_data()`
* Automatic column name normalization with `clean_column_names()`
* Robust numeric conversion with `safe_to_numeric()`
* Defensive handling of malformed or inconsistent data
* Clean, reusable preprocessing functions

---

## 📂 Project Structure

```
Week 4.ipynb
```

Core functions:

```python
load_data()
clean_column_names()
safe_to_numeric()
```

---

## 📦 Dependencies

Install the required packages:

```bash
pip install pandas numpy
```

Imported libraries:

* pandas
* numpy
* pathlib

---

## ⚙️ How It Works

### 1️⃣ Load Dataset

```python
df = load_data("path/to/file.csv")
```

Handles structured file loading safely.

---

### 2️⃣ Clean Column Names

```python
df = clean_column_names(df)
```

Standardizes columns by:

* Lowercasing
* Removing extra spaces
* Normalizing naming format

---

### 3️⃣ Safe Numeric Conversion

```python
df["column"] = safe_to_numeric(df["column"])
```

Converts values safely while handling:

* Invalid strings
* Missing values
* Mixed data types

---

## 🎯 Use Cases

* Data preprocessing for ML models
* Data cleaning pipelines
* Preparing financial or operational datasets
* Structured data ingestion workflows

---

## 🚀 Next Steps

You can extend this notebook by:

* Adding validation schemas
* Logging transformation steps
* Converting it into a reusable Python module
* Integrating into a FastAPI or Django backend

---
