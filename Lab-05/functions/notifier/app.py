import redis

r = redis.Redis(host="redis", port=6379)
pubsub = r.pubsub()
pubsub.subscribe("notify")

print("Notifier started...", flush=True)

for msg in pubsub.listen():
    if msg["type"] == "message":
        filename = msg["data"].decode()
        print(f"Notification: {filename} processed")