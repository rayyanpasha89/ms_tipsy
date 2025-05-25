from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from rag_engine import get_response

app = FastAPI(
    title="Ms Tipsy Backend",
    description="Backend for Ms Tipsy, the Indian public school AI assistant.",
    version="1.1.0",
)

# For development, allow all origins. Restrict in production!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    """
    Receives a question and returns an answer from the AI model.
    Expects: { "prompt": "your question" }
    """
    data = await request.json()
    prompt = data.get("prompt", "hello")
    response = get_response(prompt)
    return JSONResponse({"response": response})