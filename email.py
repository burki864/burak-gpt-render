import smtplib
from email.mime.text import MIMEText

def send_2fa(to, code):
    msg = MIMEText(f"BurakGPT doğrulama kodun: {code}")
    msg["Subject"] = "BurakGPT 2FA"
    msg["From"] = "burakgpthelpcenter@gmail.com"
    msg["To"] = to

    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login("burakgpthelpcenter@gmail.com", "APP_PASSWORD")
    s.send_message(msg)
    s.quit()
