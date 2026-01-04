from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.auth import router as auth_router, get_user
from backend.llm import ask_llm

app = FastAPI(title="BurakGPT LOCAL 🧠")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"]
)

app.include_router(auth_router, prefix="/auth")


class ChatReq(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatReq, user=Depends(get_user)):
    prompt = f"""
Kullanıcı: {user['email']}
Soru: {req.message}
Cevabı samimi ve net ver.
"""
    answer = ask_llm(prompt)

    return {
        "reply": answer
    }


@app.get("/")
def root():
    return {"status": "LOCAL AI ayakta kral 🚀"}
