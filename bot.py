import schedule
import time
import datetime
from parser import parse_data
from DataCleaning import clean_data
from write import write_to_sheets

def main():
    start_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\n🕒 [{start_time}] Starting data parsing and update...")

    try:
        raw = parse_data()
        print(f"📦 Received {len(raw)} rows of data")

        clean = clean_data(raw)
        print(f"🧹 Cleaned data: {len(clean)} rows remaining")

        write_to_sheets(clean)
        print("✅ Data successfully written to Google Sheets!")

    except Exception as e:
        print(f"❌ Error: {e}")

    end_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"🏁 Finished at {end_time}\n")

# Schedule the task every 60 minutes
schedule.every(60).minutes.do(main)

if __name__ == "__main__":
    print("🚀 Google Sheets Bot started. Updates every 60 minutes.")
    main()  # run once at startup

    while True:
        schedule.run_pending()

        # Countdown visualization (minutes + seconds)
        next_run = schedule.next_run()
        if next_run:
            wait_seconds = int((next_run - datetime.datetime.now()).total_seconds())
            for remaining in range(wait_seconds, 0, -1):
                mins, secs = divmod(remaining, 60)
                print(f"\r⏳ Next update in {mins:02d}:{secs:02d}", end="")
                time.sleep(1)
