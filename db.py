USERS = [
    {"email": "kral@burakgpt.ai", "name": "Burak"},
    {"email": "test@test.com", "name": "Test"}
]


def get_user_by_email(email: str):
    for u in USERS:
        if u["email"] == email:
            return u
    return None
