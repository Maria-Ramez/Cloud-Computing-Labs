import time
import os
import redis

r = redis.Redis(host="redis", port=6379)

INPUT_DIR = "/data/input"

print("Watching for new images...", flush=True)

seen = set()

while True:
    files = os.listdir(INPUT_DIR)
    for f in files:
        if f not in seen:
            print(f"New file detected: {f}")
            r.publish("events", f)
            seen.add(f)
    time.sleep(2)