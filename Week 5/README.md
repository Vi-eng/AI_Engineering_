**Semantic Search with Sentence Transformers + FAISS**

## 📌 Overview

This notebook demonstrates how to build a **semantic search engine** using:

* `SentenceTransformer` for text embeddings
* `FAISS` for fast similarity search
* `NumPy` for vector handling

It indexes a small dataset of text documents and retrieves the most semantically similar documents using **top-k nearest neighbor search**.

---

## 🧠 What This Notebook Demonstrates

* Embedding text documents into dense vectors
* Building a FAISS index
* Performing similarity search
* Returning top-k most relevant documents

This is a foundational building block for:

* Retrieval-Augmented Generation (RAG)
* Intelligent search systems
* Document retrieval engines
* Chatbot memory systems

---

## 📂 Project Structure

```
Week 5.ipynb
```

Core function:

```python
semantic_search()
```

---

## 📦 Dependencies

Install required packages:

```bash
pip install sentence-transformers faiss-cpu numpy
```

Imported libraries:

* sentence_transformers
* faiss
* numpy

---

## ⚙️ How It Works

### 1️⃣ Load Embedding Model

```python
model = SentenceTransformer("model-name")
```

Encodes text into dense vector representations.

---

### 2️⃣ Embed Documents

```python
embeddings = model.encode(documents)
```

Transforms raw text into numerical vectors.

---

### 3️⃣ Build FAISS Index

```python
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
```

Stores vectors in a similarity-searchable structure.

---

### 4️⃣ Run Semantic Search

```python
semantic_search(query, index, model, documents, top_k=3)
```

Returns the most semantically similar documents to a given query.

---

## 🔍 Example Use Case

Query:

```
"How do I implement vector search?"
```

Returns:

* Top 3 semantically similar documents
* Ranked by similarity distance

---

## 🎯 Applications

* RAG pipelines
* Knowledge-base search
* Internal document retrieval
* AI assistants
* FAQ bots

---

## 🚀 Possible Extensions

* Replace small dataset with large corpus
* Persist FAISS index to disk
* Use cosine similarity instead of L2
* Integrate with FastAPI backend
* Add OpenAI or Groq for answer generation

---