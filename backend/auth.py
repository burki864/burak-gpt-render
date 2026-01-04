from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from db import SessionLocal, User
import random
from email import send_2fa

router = APIRouter()
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(email: str, password: str):
    db = SessionLocal()
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(400, "Email already registered")

    hashed = pwd.hash(password)
    code = str(random.randint(100000, 999999))

    user = User(email=email, password=hashed, twofa_code=code)
    db.add(user)
    db.commit()

    send_2fa(email, code)
    return {"message": "Verification code sent"}

@router.post("/verify")
def verify(email: str, code: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()

    if not user or user.twofa_code != code:
        raise HTTPException(400, "Invalid code")

    user.is_verified = True
    user.twofa_code = None
    db.commit()

    return {"message": "Account verified"}

@router.post("/login")
def login(email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()

    if not user or not pwd.verify(password, user.password):
        raise HTTPException(401, "Invalid credentials")

    if not user.is_verified:
        code = str(random.randint(100000, 999999))
        user.twofa_code = code
        db.commit()
        send_2fa(email, code)
        return {"twofa": True}

    return {"success": True}
