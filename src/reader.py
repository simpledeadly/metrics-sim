import psycopg2
import os

def get_events():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname=os.getenv("DB_NAME", "ragmetrics"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "pass"),
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM rag_events")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def print_events():
    events = get_events()
    for row in events:
        print(row)

if __name__ == "__main__":
    print_events()
