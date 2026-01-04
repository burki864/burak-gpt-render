from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import time

from backend.auth import router as auth_router, get_user
from backend.db import init_db

# --------------------------------------------------
# APP INIT
# --------------------------------------------------
app = FastAPI(
    title="BurakGPT API",
    description="BurakGPT resmi backend servisi",
    version="1.0.0"
)

# --------------------------------------------------
# DB INIT (Render startup safe)
# --------------------------------------------------
init_db()

# --------------------------------------------------
# MIDDLEWARES
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # prod'da domain kısıtlanır
    allow_headers=["*"],
    allow_methods=["*"]
)

# --------------------------------------------------
# ROUTERS
# --------------------------------------------------
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

# --------------------------------------------------
# MODELS
# --------------------------------------------------
class ChatReq(BaseModel):
    message: str

class ChatRes(BaseModel):
    reply: str
    timestamp: str
    latency_ms: int

# --------------------------------------------------
# HEALTHCHECK (gönlümden kopan parça ❤️)
# Render, uptime robot, load balancer sever
# --------------------------------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "burakgpt-backend",
        "time": datetime.utcnow().isoformat() + "Z"
    }

# --------------------------------------------------
# CHAT ENDPOINT (JWT + 2FA doğrulanmış user)
# --------------------------------------------------
@app.post("/chat", response_model=ChatRes)
def chat(req: ChatReq, user=Depends(get_user)):
    start = time.time()

    # burada ileride LLM / OpenAI / worker bağlanacak
    reply_text = f"{user['email']} dedi ki: {req.message}"

    latency = int((time.time() - start) * 1000)

    return {
        "reply": reply_text,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "latency_ms": latency
    }
