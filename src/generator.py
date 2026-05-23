import random
import json
from datetime import datetime

MODELS = ["qwen", "gemma"]
QUERIES = [
    "что такое RAG",
    "как работает эмбеддинг",
    "токенизация текста",
    "векторная база данных",
]

def generate_event():
    return {
        "query": random.choice(QUERIES),
        "model": random.choice(MODELS),
        "latency_ms": random.randint(80, 400),
        "relevance_score": round(random.uniform(0.6, 1.0), 2),
        "created_at": datetime.now().isoformat(),
    }

if __name__ == "__main__":
    for _ in range(5):
        event = generate_event()
        print(json.dumps(event, ensure_ascii=False))
