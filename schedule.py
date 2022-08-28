from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timezone, timedelta
import time

from schedule.exchange_rate_job import get_and_save_exchange_rate
from sendEmail.send_email import send_email

scheduler = BackgroundScheduler()

print("Run schedule.py at %s" % datetime.now(timezone.utc))

try:
    print("Add Jobs to Scheduler at %s" % datetime.now(timezone.utc))

    #每週一 ~ 五 18:00 ，由網路抓匯率與存匯率至DB
    scheduler.add_job(get_and_save_exchange_rate, 'cron', day_of_week = '1-5', hour = 18, minute = 0, timezone = 'Asia/Taipei')
    scheduler.start()

    while True:
            time.sleep(5)

except Exception as e:
    scheduler.shutdown()

    now = datetime.now(timezone.utc)
    local_datetime = now + timedelta(hours = 8)

    title = "Run scheduler Failure"
    content = "Run scheduler Failure at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
    send_email(title, content)
