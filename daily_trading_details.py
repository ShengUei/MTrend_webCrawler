from datetime import datetime, timedelta

from util.request import get_request
from logger.logger import get_logger

def get_daily_trading_details():
    utc_now = datetime.utcnow()
    local_datetime = utc_now + timedelta(hours = 8)
    local_weekday = local_datetime.isoweekday()
    date_str = local_datetime.strftime('%Y%m%d')

    HOST = 'www.twse.com.tw'
    url = 'https://www.twse.com.tw/en/fund/T86?response=json&date={0}&selectType=ALL'.format(date_str)
    stat_code = {0: 'OK', 1: 'No Data!'}

    logger = get_logger()

    try:
        if(local_weekday > 5):
            print('Today is holiday.')
            logger.info('Today is holiday.')
            return None

        res_dict = get_request(url, HOST)

        if(res_dict == None):
            print('Get Data Failures From web.')
            logger.error('Get Data Failures From web.')
            return None
        
        if(res_dict['stat'] != stat_code[0]):
            print('No data.')
            logger.error('No data.')
            return None

    except Exception as e:
        print("Excetion $s", e)
        logger.error("Exception : %s" % e)
        return None

    else:
        print("Get Daily Trading Details Success From web")
        logger.info("Get Daily Trading Details Success From web")
        return res_dict['data']

