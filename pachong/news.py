import os
import re
import string
import sys
import time
from urllib import request

import requests
from bs4 import BeautifulSoup


url = 'https://news.sina.com.cn/society/'


def getDetail(news_url, news_title):
    req = request.Request(news_url)
    res = request.urlopen(req)
    soup = BeautifulSoup(res.read(), "html.parser")
    news_time = soup.select(".date")[0].text
    news_content = soup.select("#article")[0].text
    news_from = soup.select(".source")[0].text
    # print(news_url)
    u = news_url.split(".")[-2].split("/")[-1][5:]
    json_url = "https://comment.sina.com.cn/page/info?version=1&format=json&channel=sh&newsid=comos-{}" \
               "&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3".format(u)
    jason = requests.get(json_url).json()
    if jason:
        pinglun = jason["result"]["count"]["total"]
        canyu = jason.get("result").get("count").get("show")
        print("{}条评论 | {}人参与".format(pinglun, canyu))
    txtPath = sys.path[0]+'/news/'+news_title+'.txt'
    # with open(txtPath, "w", encoding="utf-8") as f:
    #     f.write(news_time+'  '+news_from+'\n'+news_content)

    pic =soup.select("#article img")
    for p in pic:
        dirPath = sys.path[0]+'/news/'+news_title
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)
        picPath = dirPath + '/'+p.get("src").split("/")[-1]
        pic_url = "http:"+p.get("src")
        response = requests.get(pic_url)
        picture = response.content
        # with open(picPath, "wb") as f1:
        #     f1.write(picture)


def getTitle(url):
    res = requests.get(url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "html.parser")
    titles = soup.select("ul.news-2 a")
    for t in titles:
        news_title = t.text
        news_title = re.sub("[A-Za-z\!\%\[\]\,\。\:]", "", news_title)
        print(news_title)
        news_url = t.attrs["href"]
        # print(news_title, news_url)
        getDetail(news_url, news_title)
getTitle(url)

