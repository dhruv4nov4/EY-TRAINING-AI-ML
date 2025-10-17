import pandas as pd
from queue import Queue
import logging

order_queue = Queue()

# Producer
def push_order(order):
    order_queue.put(order)
    logging.info(f"Order pushed: {order['OrderID']}")

# Consumer
def process_orders():
    while not order_queue.empty():
        order = order_queue.get()
        order["TotalPrice"] = order["Quantity"] * order["Price"]
        logging.info(f"Processed order: {order['OrderID']}")
        # Append to CSV
        pd.DataFrame([order]).to_csv("processed_orders_1.csv", mode='a', header=False, index=False)