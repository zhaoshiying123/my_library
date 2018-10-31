import time

import requests
from bs4 import BeautifulSoup


url = "http://www.ygdy8.com"


def getDetail(detai_url):
    response = requests.get(detai_url)
    response.encoding = "gb2312"
    bs = BeautifulSoup(response.text, "html.parser")
    # name = bs.select("#Zoom a")[0].text
    aaa = bs.select("#Zoom tbody td a")
    xiazai = aaa[0].get("href")
    return xiazai

def getMovies(url):
    res = requests.get(url)
    res.encoding = "gb2312"
    soup = BeautifulSoup(res.text, "html.parser")
    movies = soup.select(".co_content8 table tr td a")
    for m in movies[2::2]:
        title = m.text
        detail_href = m.attrs["href"]
        detail_url = url + detail_href
        # print(title, detail_href, detail_url)
        download = getDetail(detail_url)
        movies = {
            "电影名字": title,
            "电影的地址": detail_url,
            "电影下载地址": download
        }
        print(movies)
        time.sleep(2)
getMovies(url)
