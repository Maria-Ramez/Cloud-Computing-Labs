import requests
import time

url = "http://localhost:5000/"

times = []

for i in range(50):
    start = time.time()
    r = requests.get(url)
    end = time.time()
    response_time = end - start
    times.append(response_time)
    print(f"Request {i+1}: {response_time:.3f} seconds")

print("\nSummary:")
print(f"Min: {min(times):.3f}")
print(f"Max: {max(times):.3f}")
print(f"Average: {sum(times)/len(times):.3f}")