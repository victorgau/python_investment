import requests
import time
import json

# 參考 twstock 取得需要的 URL
SESSION_URL = 'http://mis.twse.com.tw/stock/index.jsp'
STOCKINFO_URL = 'http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={stock_id}&_={time}'


def get_realtime_quote(stockNo, ex='tse'):
    req = requests.Session()
    req.get(SESSION_URL)
    
    stock_id = '{}_{}.tw'.format(ex, stockNo)

    r = req.get(STOCKINFO_URL.format(stock_id=stock_id, time=int(time.time()) * 1000))

    try:
        return r.json()
    except json.decoder.JSONDecodeError:
        return {'rtmessage': 'json decode error', 'rtcode': '5000'}


def get_quote(symbol):
    data = get_realtime_quote(symbol)

    return float(data['msgArray'][0]['z'])
