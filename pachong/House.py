import time
import requests
from pyquery import PyQuery as pq


header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
}


def houseDetail(url):
    response = requests.get(url, headers=header).text
    docs = pq(response)
    detail = docs(".houseInfo-detail-list.clearfix")
    for d in detail.items():
        xiaoqu = d.find(".houseInfo-content a").text()
        shoufu = d.find(".houseInfo-label.text-overflow").text()
        weizhi = d.find(".loc-text").text()
        Detail = {
            "所属小区": xiaoqu,
            "参考首付": shoufu,
            "所在位置": weizhi
        }
    print(Detail)

def getHouse(ur):
    res = requests.get(ur, headers=header)
    doc = pq(res.text)
    house = doc(".list-item")
    for h in house.items():
        jianjie = h.find(".house-title").text()
        xinxi = h.find(".details-item").text()
        dizhi = h.find(".comm-address").text()
        jiage = h.find(".price-det").text()
        danjia = h.find(".unit-price").text()
        Houses = {
            "简介": jianjie,
            "详细信息": xinxi,
            "地址": dizhi,
            "总价": jiage,
            "单价": danjia,
        }
        # print(Houses)
        detail_url = h.find("a").attr("href")
        houseDetail(detail_url)


for i in range(1, 3):
    url = "https://shenzhen.anjuke.com/sale/longhuaq/p{}/#filtersort".format(i)
    getHouse(url)
    time.sleep(5)