import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # ← .env を読み込む

def get_conn():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        port=os.environ.get("DB_PORT", 5432),
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
    )

print(os.environ.get("DB_USER"))