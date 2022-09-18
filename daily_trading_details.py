from datetime import datetime, timedelta
from threading import local

from util.request import get_request

utc_now = datetime.utcnow()
local_datetime = utc_now + timedelta(hours = 8)
local_weekday = local_datetime.isoweekday()
date_str = local_datetime.strftime('%Y%m%d')

HOST = 'www.twse.com.tw'
url = 'https://www.twse.com.tw/en/fund/T86?response=json&date={0}&selectType=ALL'.format(date_str)

def test_method(url, HOST):
    dict = {'data': None, 'error_msg': None}
    stat_code = {0: 'OK', 1: 'No Data!'}
    res_dict = get_request(url, HOST)

    if(local_weekday > 5):
        dict['error_msg'] = 'Today is holiday.'
        return dict

    if(res_dict['stat'] != stat_code[0]):
        dict['error_msg'] = 'No data.'
        return dict

    dict['data'] = res_dict['data']
    
    return dict

result = test_method(url, HOST)

if(result['data'] == None):
    print(result['error_msg'])