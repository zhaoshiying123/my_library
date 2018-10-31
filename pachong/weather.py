import time
import pymongo
import requests
from bs4 import BeautifulSoup


client = pymongo.MongoClient(host='localhost', port=27017)
# 指定数据库
mgdb = client.weather
# 表名
coll = mgdb.tianqi


def getWeather():
    url = "http://tianqi.sogou.com/?tid=101280601"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    wendu = soup.select(".num")[0].text
    tianqi = soup.select(".text")[0].text
    shijian = soup.select(".row2.row2-0 .date")[0].text
    fengxiang = soup.select(".wind")[0].text
    shidu = soup.select(".hundity")[0].text
    # zhishu = soup.select("span .livindex").text

    weather = {
        "温度": wendu,
        "天气": tianqi,
        "时间": shijian,
        "风向": fengxiang,
        "湿度": shidu,
        # "指数": zhishu
    }
    # 向mongodb的表中增加数据
    coll.insert(weather)
    print(weather)


while True:
    getWeather()
    time.sleep(5)