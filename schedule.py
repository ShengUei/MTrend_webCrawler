from apscheduler.schedulers.background import BlockingScheduler
from datetime import datetime, timezone, timedelta

from schedule.exchange_rate_job import get_and_save_exchange_rate
from schedule.trading_details_job import get_and_save_trading_details
from sendEmail.send_email import send_email

scheduler = BlockingScheduler()

print("Run schedule.py at %s" % datetime.now(timezone.utc))

try:
    print("Add Jobs to Scheduler at %s" % datetime.now(timezone.utc))

    #每週一 ~ 五 18:00 ，由網路抓匯率與存匯率至DB
    scheduler.add_job(get_and_save_exchange_rate, 'cron', day_of_week = 'mon-fri', hour = 18, minute = 0, timezone = 'Asia/Taipei')

    #每天 18:00 ，由網路抓三大法人交易量與三大法人交易量至DB
    scheduler.add_job(get_and_save_trading_details, 'cron', day_of_week = 'mon-fri', hour = 18, minute = 10, timezone = 'Asia/Taipei')

    scheduler.start()

except Exception as e:
    scheduler.shutdown()

    now = datetime.now(timezone.utc)
    local_datetime = now + timedelta(hours = 8)

    title = "Run scheduler Failure"
    content = "Run scheduler Failure at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
    send_email(title, content)
