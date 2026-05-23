import psycopg2
import os

def init():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname=os.getenv("DB_NAME", "ragmetrics"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "pass"),
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS rag_events (
            id SERIAL PRIMARY KEY,
            query TEXT,
            model VARCHAR(50),
            latency_ms INTEGER,
            relevance_score FLOAT,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("DB initialized.")

if __name__ == "__main__":
    init()
