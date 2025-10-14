import threading
import queue
import time
import random

# Shared queue
q = queue.Queue()

# Producer function
def producer():
    for i in range(10):
        item = random.randint(1, 100)
        print(f"Producer produced: {item}")
        q.put(item)
        time.sleep(random.uniform(0.5, 1.5))  # Simulate variable production time

# Consumer function
def consumer():
    while True:
        item = q.get()
        print(f"Consumer consumed: {item}")
        q.task_done()
        time.sleep(random.uniform(0.5, 1.0))  # Simulate variable consumption time

# Main function
def main():
    # Create threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer, daemon=True)

    # Start threads
    producer_thread.start()
    consumer_thread.start()

    # Wait for producer to finish
    producer_thread.join()

    # Wait until all items are processed
    q.join()
    print("All items have been consumed.")

if __name__ == "__main__":
    main()