import time
import requests
from pyquery import PyQuery as pq
import pymongo


def getWeather():
    url = "http://pc.weathercn.com/weather/day/58194?date=20181018&partner=&p_source=&p_type=jump&areatype="
    res = requests.get(url)
    query = pq(res.text)
    tianqi = query(".weather-card-day .weather-infos .weather-icon-wrap").text()
    details = query(".weather-card-day .weather-infos .weather-details")
    for d in details:
        wendu = d.(".detail-value")[0].text()
        tigan = d(".detail-value")[1].text()
        # gailv = d("").text()
        # yunliang = d("div:nth-child(4)").text()
        # feng_min = d("div:nth-child(5)").text()
        # feng_max = d("div:last-child").text()
    weather = {
        "天气": tianqi,
        "温度": wendu,
        "体感温度": tigan,
        # "降水概率": gailv,
        # "云量": yunliang,
        # "最小风": feng_min,
        # "最大风": feng_max
    }
    print(weather)


while True:
    getWeather()
    time.sleep(5)