from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

# PostgreSQL connection details
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "day34db")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "secret123")

# Redis connection details
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

@app.route("/")
def home():
    return "Hello from Day 34! Version 2 - Rebuilt Successfully!"

@app.route("/db")
def database():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cur = conn.cursor()
        cur.execute("SELECT version();")
        result = cur.fetchone()

        cur.close()
        conn.close()

        return f"PostgreSQL Connected! Version: {result[0]}"

    except Exception as e:
        return f"Database connection failed: {e}", 500

@app.route("/redis")
def cache():
    try:
        r = redis.Redis(
            host=REDIS_HOST,
            port=6379,
            decode_responses=True
        )

        r.set("message", "Hello from Redis!")
        result = r.get("message")

        return f"Redis Connected! Message: {result}"

    except Exception as e:
        return f"Redis connection failed: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
