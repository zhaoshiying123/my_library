import time
import requests
from bs4 import BeautifulSoup


url0 = ("http://pc.weathercn.com/weather/day/58194?date=20181019&partner=&p_source=&p_type=jump&areatype=")
res0 = requests.get(url0)
soup0 = BeautifulSoup(res0.text, "html.parser")
riqi = soup0.select("select [selected]")
shijian = soup0.select(".huangli-time")[0].select("p")
year = int(shijian[0].text[0:4])
month = int(shijian[0].text[5:7])
day = int(shijian[1].text)


def getWeather(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    tianqi = soup.select(".weather-card-day .weather-icon-wrap")[0].text
    feng = soup.select(".weather-card-day .weather-details")[0].select(".detail-item")
    wen = soup.select(".weather-card-day .weather-details")[0].select(".detail-value")
    # print(wen)
    wendu = wen[0].text
    tigan = wen[1].text
    jiangshui = wen[2].text
    yunliang = wen[3].text
    fengxiang_min = feng[4].select("p")[0].text
    feng_min = wen[4].text
    fengxiang_max = feng[5].select("p")[0].text
    feng_max = wen[5].text
    weather = {
        "日期": riqi[0].text,
        "时间": "{}年{}月{}日".format(year, month, day),
        "天气": tianqi,
        "温度": wendu,
        "体感温度": tigan,
        "降水概率": jiangshui,
        "云量": yunliang,
        "小风": [fengxiang_min, feng_min],
        "大风": [fengxiang_max, feng_max]
    }
    print(weather)


count = 1
while True:
    url = "http://pc.weathercn.com/weather/day/58194" \
          "?date={}{}{}&partner=&p_source=&p_type=jump&areatype=".format(year, month, day)
    day += 1
    if day > 31:
        day = 1
        month += 1
    if month > 12:
            month = 1
            year += 1
    getWeather(url)
    count += 1
    if count > 15:
        break
    time.sleep(3)
