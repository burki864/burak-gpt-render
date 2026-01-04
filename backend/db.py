import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# tablo referansı
users = supabase.table("users")

def init_db():
    # Render startup sırasında çağrılır
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError("Supabase env variables missing")
    return True
