import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
DB_URL = os.getenv("DB_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")
AUTH_USERS = set(int(x) for x in os.getenv("AUTH_USERS", "").split())

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DB_URL:
    print("No DB_URL found. Exiting...")
    raise SystemExit
if not AUTH_USERS:
    print("No AUTH_USERS found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DB_URL and 'postgresql' not in DB_URL:
    DB_URL = DB_URL.replace("postgres", "postgresql")
