from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timezone

from schedule.exchange_rate_job import get_and_save_exchange_rate
from schedule.running import show_running
from sendEmail.send_email import send_email

scheduler = BackgroundScheduler()

try:
    #每週一 ~ 五 18:00 ，由網路抓匯率與存匯率至DB
    scheduler.add_job(get_and_save_exchange_rate, 'cron', day_of_week = '1-5', hour = 18, minute = 0, timezone = 'Asia/Taipei')
    scheduler.add_job(show_running,'interval', minutes = 60)
    scheduler.start()

except Exception as e:
    scheduler.shutdown()

    print("Exception %s at %s", e, datetime.now(timezone.utc))

    title = "Run scheduler Failure"
    content = "Run scheduler Failure at {}".format(datetime.now(timezone.utcoffset(+8)))
    send_email(title, content)
