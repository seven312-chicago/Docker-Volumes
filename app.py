import os
import time
from datetime import datetime

# Define the directory and file path
DATA_DIR = "/data"
FILE_PATH = os.path.join(DATA_DIR, "log.txt")

# Create the directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Open the file in append mode and continuously write a timestamp
try:
    with open(FILE_PATH, "a") as f:
        print(f"Starting to write timestamps to {FILE_PATH}...")
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"[{timestamp}] Data written successfully.\n"
            f.write(message)
            f.flush() # Ensure the data is written to the file immediately
            print(f"Written: {message.strip()}")
            time.sleep(2) # Write every 2 seconds
except KeyboardInterrupt:
    print("\nScript terminated by user.")
except Exception as e:
    print(f"An error occurred: {e}")