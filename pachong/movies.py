import sys
import time
import requests


url = "https://box.maoyan.com/promovie/api/box/second.json"
def getMovies():
    res = requests.get(url)
    if res.status_code == 200:
        film_data = res.json()
    else:
        print("获取数据错误")
    if film_data:
        films = film_data.get("data").get("list")
        for item in films:
            film = {}
            film["影片"] = item.get("movieName")
            film["上映天数"] = item.get("releaseInfo")
            film["总票房"] = item.get("sumBoxInfo")
            film["综合票房"] = item.get("boxInfo")
            film["票房占比"] = item.get("boxRate")
            film["排片场次"] = item.get("showInfo")
            film["排片占比"] = item.get("showRate")
            film["场均人次"] = item.get("avgShowView")
            film["上座率"] = item.get("avgSeatView")
            print(film)

while True:
    getMovies()
    time.sleep(3)