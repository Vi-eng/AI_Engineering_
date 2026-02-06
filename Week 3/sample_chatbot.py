import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("Please set GROQ_API_KEY in your .env file")

# 1. Document Processing
with open("data.txt", 'r', encoding='utf-8') as f:
    data = f.read()

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
documents = splitter.create_documents([data])

# 2. Embeddings & VectorStore (Keeping HF for embeddings as they run locally)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 3. Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    groq_api_key=groq_api_key
)

# 4. Build the Chain (Modern LCEL Way - No 'langchain.chains' needed)
prompt = ChatPromptTemplate.from_template("""
Answer the question based ONLY on the following context:
{context}

Question: {input}
Answer:""")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# This pipe syntax is the new standard
rag_chain = (
    {"context": retriever | format_docs, "input": RunnablePassthrough()}
    | prompt 
    | llm 
    | StrOutputParser()
)

# 5. Interactive Loop
print("\n" + "="*30)
print("Groq Chatbot Active!")
print("="*30 + "\n")

while True:
    query = input("You: ").strip()
    if query.lower() in ['exit', 'quit']:
        print("Chatbot: Goodbye!")
        break
    if not query: continue

    try:
        response = rag_chain.invoke(query)
        print(f"Chatbot: {response}\n")
    except Exception as e:
        print(f"Error: {e}\n")