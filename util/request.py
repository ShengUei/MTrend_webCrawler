import random
import requests
import json

CHROME = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
EDGE = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/104.0.1293.70'
web_browser_list = [CHROME, EDGE]

def get_request(target_url, host):
    res = requests.get(url = target_url,
                    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,text/javascript, */*; q=0.01", 
                                "Accept-Encoding": "gzip, deflate, br", 
                                "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6", 
                                "Host": host,  #目標網站 
                                "Sec-Fetch-Dest": "document", 
                                "Sec-Fetch-Mode": "navigate", 
                                "Sec-Fetch-Site": "none", 
                                "Upgrade-Insecure-Requests": "1",
                                "user-agent" : random.choice(web_browser_list),
                                "Referer": "https://www.google.com/"})
    
    return json.loads(res.text)
