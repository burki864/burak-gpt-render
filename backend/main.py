from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.auth import router as auth_router, get_user

app = FastAPI(title="BurakGPT Backend 🧠🔥")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

app.include_router(auth_router, prefix="/auth")


class ChatReq(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatReq, user=Depends(get_user)):
    return {
        "reply": f"👑 {user['email']} dedi ki: {req.message}\n🤖 Cevap: Selam kral, buradayım."
    }


@app.get("/")
def root():
    return {"status": "BurakGPT ayakta 🚀"}
