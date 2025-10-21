import time
import logging

logging.basicConfig(filename="order_log.log", level=logging.INFO)

start = time.time()
try:
    # ETL logic here
    logging.info("ETL started")
    # ...
    logging.info("ETL completed")
except Exception as e:
    logging.error(f"Error: {str(e)}")

end = time.time()
logging.info(f"ETL Duration: {end - start:.2f} seconds")