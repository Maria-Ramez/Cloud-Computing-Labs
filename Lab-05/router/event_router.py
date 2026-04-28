import redis

r = redis.Redis(host="redis", port=6379)
pubsub = r.pubsub()
pubsub.subscribe("events")

print("Router listening for events...", flush=True)

for message in pubsub.listen():
    if message["type"] == "message":
        file_name = message["data"].decode()
        print(f"Routing event for: {file_name}")

        r.publish("resize", file_name)
        r.publish("notify", file_name)