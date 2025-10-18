import schedule
import time

def main():
    print("⏳ Парсим и обновляем данные...")
    # тут твой код парсинга и записи в таблицу
    print("✅ Обновление завершено")

# Запускать каждые 60 минут
schedule.every(60).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(60)