from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.db import get_user_by_email

router = APIRouter()
security = HTTPBearer()


def get_user(creds: HTTPAuthorizationCredentials = Depends(security)):
    token = creds.credentials
    user = get_user_by_email(token)

    if not user:
        raise HTTPException(status_code=401, detail="Yetkisiz")

    return user


@router.post("/login")
def login(email: str):
    user = get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı yok")

    return {"access_token": email}
