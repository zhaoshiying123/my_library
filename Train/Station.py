# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/29 10:15
# @Author : 'Sean'
# @File   : Station.py
import requests
stations = {}
res = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971')
print(res.status_code)
t = res.text
li1 = t.split('@')
li1.remove(li1[0])
for i in li1:
    li2 = i.split('|')
    stations[li2[1]] = li2[2]
print(stations)

