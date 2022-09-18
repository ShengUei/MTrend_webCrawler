from datetime import datetime, timedelta
from threading import local

from util.request import get_request

utc_now = datetime.utcnow()
local_datetime = utc_now + timedelta(hours = 8)
local_weekday = local_datetime.isoweekday()
date_str = local_datetime.strftime('%Y%m%d')

HOST = 'www.twse.com.tw'
url = 'https://www.twse.com.tw/en/fund/T86?response=json&date={0}&selectType=ALL'.format(date_str)
# url = 'https://www.twse.com.tw/en/fund/T86?response=json&date=20220916&selectType=ALL'
stat_code = {0: 'OK', 1: 'No Data!'}

res_dict = get_request(url, HOST)

if(res_dict['stat'] == stat_code[0]):
    print(res_dict['data'])
else:
    print('No Data!')