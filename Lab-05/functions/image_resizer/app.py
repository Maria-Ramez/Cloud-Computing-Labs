import redis
from PIL import Image
import os

r = redis.Redis(host="redis", port=6379)
pubsub = r.pubsub()
pubsub.subscribe("resize")

INPUT = "/data/input"
OUTPUT = "/data/output"

print("Image Resizer started...", flush=True)

for msg in pubsub.listen():
    if msg["type"] == "message":
        filename = msg["data"].decode()
        print(f"Resizing {filename}")

        try:
            img = Image.open(os.path.join(INPUT, filename))
            img = img.resize((100, 100))
            img.save(os.path.join(OUTPUT, filename))
            print("Image resized successfully")
        except Exception as e:
            print("Error:", e)