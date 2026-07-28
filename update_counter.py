import os
from datetime import datetime

COUNTER_FILE = "counter.txt"

# Create file if it doesn't exist
if not os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "w") as f:
        f.write("0")

# Read current value
with open(COUNTER_FILE, "r") as f:
    count = int(f.read().strip())

# Increment
count += 1

# Write new value
with open(COUNTER_FILE, "w") as f:
    f.write(str(count))

print(f"Counter updated to {count}")

# Optional: Log timestamp
with open("history.log", "a") as log:
    log.write(f"{datetime.now()} - Counter: {count}\n")