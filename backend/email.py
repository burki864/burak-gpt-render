import smtplib
from email.message import EmailMessage
import os

EMAIL = "burakgpthelpcenter@gmail.com"
PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_2fa(email: str, code: str):
    msg = EmailMessage()
    msg["Subject"] = "BurakGPT Doğrulama Kodu"
    msg["From"] = EMAIL
    msg["To"] = email
    msg.set_content(f"Giriş doğrulama kodunuz: {code}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
