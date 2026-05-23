def summary(events):
    if not events:
        return {}
    scores = [e[4] for e in events]
    latencies = [e[3] for e in events]
    return {
        "count": len(events),
        "avg_score": round(sum(scores) / len(scores), 2),
        "avg_latency": round(sum(latencies) / len(latencies), 1),
    }

def worst_queries(events, threshold=0.75):
    return [e for e in events if e[4] < threshold]
