from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from passlib.hash import bcrypt
import os
import time
from backend.db import users
from backend.email import send_2fa

router = APIRouter()
security = HTTPBearer()
SECRET = os.getenv("JWT_SECRET","secret")

@router.post("/signup")
def signup(data: dict):
    if data["email"] in users:
        raise HTTPException(400,"Zaten kayıtlı")
    code = str(time.time())[-6:]
    users[data["email"]] = {
        "password": bcrypt.hash(data["password"]),
        "code": code,
        "verified": False
    }
    send_2fa(data["email"], code)
    return {"ok": True}

@router.post("/login")
def login(data: dict):
    u = users.get(data["email"])
    if not u or not bcrypt.verify(data["password"], u["password"]):
        raise HTTPException(401,"Hatalı giriş")
    token = jwt.encode({"email":data["email"]}, SECRET)
    return {"token": token}

def get_user(token=Depends(security)):
    try:
        payload = jwt.decode(token.credentials, SECRET)
        return payload
    except:
        raise HTTPException(401,"Yetkisiz")
