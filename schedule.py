from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timezone, timedelta

from schedule.exchange_rate_job import get_and_save_exchange_rate
from sendEmail.send_email import send_email

scheduler = BackgroundScheduler()
# scheduler = BlockingScheduler()

def running():
    print("This scheduler still running at %s" % datetime.now(timezone.utc))

print("Run schedule.py at %s" % datetime.now(timezone.utc))

try:
    print("Add Jobs to Scheduler at %s" % datetime.now(timezone.utc))
    scheduler.add_job(running, 'interval', seconds = 5)

    #每週一 ~ 五 18:00 ，由網路抓匯率與存匯率至DB
    scheduler.add_job(get_and_save_exchange_rate, 'cron', day_of_week = '1-5', hour = 18, minute = 0, timezone = 'Asia/Taipei')
    scheduler.start()

except Exception as e:
    scheduler.shutdown()

    now = datetime.now(timezone.utc)
    local_datetime = now + timedelta(hours = 8)

    title = "Run scheduler Failure"
    content = "Run scheduler Failure at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
    send_email(title, content)
