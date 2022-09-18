from util.request import get_request

URL = 'https://www.twse.com.tw/en/fund/T86?response=json&date=20220916&selectType=ALL'
HOST = 'www.twse.com.tw'

print(get_request(URL, HOST))
