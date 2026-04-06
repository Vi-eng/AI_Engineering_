# api.py
import uvicorn
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from agent import run_agent
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="PDF/Text Chatbot API")

# Enable CORS for testing with frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the static folder
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.post("/chat")
async def chat(
    user_input: Optional[str] = Form(None),
    pdf_file: Optional[UploadFile] = File(None),
    session_id: Optional[str] = Form(None)
):
    """
    Endpoint to send user messages or PDF files to the agent.
    Returns JSON with session_id, response, and history_length.
    """
    try:
        pdf_path = None
        if pdf_file:
            pdf_path = f"temp_{pdf_file.filename}"
            with open(pdf_path, "wb") as f:
                f.write(await pdf_file.read())

        result = run_agent(user_input=user_input or "", session_id=session_id, pdf_path=pdf_path)

        # Clean up temporary PDF
        if pdf_path:
            import os
            os.remove(pdf_path)

        return result

    except Exception as e:
        return {"session_id": session_id, "response": f"⚠️ Error: {str(e)}"}

@app.get("/health")
async def health():
    return {"status": "ok"}

from fastapi.responses import RedirectResponse

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)