import time
import requests
from pyquery import PyQuery as pq
import pymongo


client = pymongo.MongoClient(host="127.0.0.1")
mgdb = client.weather1
coll = mgdb.tianqi1


def getWeather():
    url = "http://tianqi.sogou.com/?tid=101280601"
    res = requests.get(url)
    query = pq(res.text)
    wendu = query(".num").text()
    tianqi = query(".r1-img").text()
    shijian = query(".row2.row2-0 .date").text()
    fengxiang = query(".condition .wind").text()
    shidu = query(".hundity").text()
    zhishu = query(".livindex").text()

    weather = {
        "温度": wendu,
        "天气": tianqi,
        "时间": shijian,
        "风向": fengxiang,
        "湿度": shidu,
        "指数": zhishu
    }
    coll.insert(weather)
    print(weather)


while True:
    getWeather()
    time.sleep(5)