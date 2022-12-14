from datetime import datetime, timezone, timedelta

from sendEmail.send_email import send_email
from webCrawler.trading_details import get_daily_trading_details
from dataAccess.postgresql.data_access import insert_all_trading_details
from dataAccess.postgresql.data_access import insert_trading_details
from util.batch import insert_batch

def get_and_save_trading_details():
    data_dict = get_daily_trading_details()

    now = datetime.now(timezone.utc)
    local_datetime = now + timedelta(hours = 8)

    if not data_dict:
        
        title = "Get Daily Trading Details Failure From web"
        content = "Get Daily Trading Details Failure From web at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
        send_email(title, content)
    
    else:
        insert_all_trading_details(data_dict)
        # insert_batch(insert_trading_details, data_dict['data_list'], data_dict['current_datetime'])
        
        title = "Get Daily Trading Details Success From web"
        content = "Get Daily Trading Details Success From web at {}".format(local_datetime.strftime('%Y/%m/%d %H:%M:%S'))
        send_email(title, content)