import schedule
import datetime

def run_etl():
    # ETL logic
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d")
    merged.to_csv(f"daily_orders_report_{timestamp}.csv", index=False)

schedule.every().day.at("07:00").do(run_etl)

while True:
    schedule.run_pending()