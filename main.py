from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.llm import ask_llm

app = FastAPI(title="BurakGPT")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"]
)

class ChatReq(BaseModel):
    message: str

@app.get("/")
def health():
    return {"status": "BurakGPT ayakta 🟢"}

@app.post("/chat")
def chat(req: ChatReq):
    answer = ask_llm(req.message)
    return {"reply": answer}
