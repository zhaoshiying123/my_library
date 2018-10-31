# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/29 15:47
# @Author : 'Sean'
# @File   : Table.py
'''
Usage:
       GetTrainTicket <beg> <end> <date>
'''
from Train.Station import stations
# from docopt import docopt
import json
import requests
from  prettytable import PrettyTable
# from  Train.Input import *

beg = stations['深圳']
end = stations['桂林']
date = '2018-09-10'
re = requests.get('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+date+
                  '&leftTicketDTO.from_station='+beg+
                  '&leftTicketDTO.to_station='+end+
                  '&purpose_codes=ADULT')
print(re.text)
jn  = json.loads(re.text)
result = jn['data']['result']
map1 = jn['data']['map']
print(map1)
pt = PrettyTable()
pt.field_names = ['车次','车站','时间','历时','商务座/特等座','一等座','二等座','高级软卧','软卧','动卧','硬卧','软座','硬座','无座']
# date = '2018-09-10'
for i in result:
    li = i.split('|')
    price_url = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=' +li[2]+ \
                '&from_station_no=' +li[16]+ \
                '&to_station_no=' +li[17]+ \
                '&seat_types=O9MO&train_date=' +date
    price = requests.get(price_url)
    price_jn = json.loads(price.text)['data']
    # print(price_jn)
    pt.add_row([
        li[3],  # 车次
        ('始'+' '+map1[li[6]]+'\n'+'终'+' '+map1[li[7]]),  # 车站
        (li[8]+'\n'+li[9]),  # 时间
        li[10],  # 历时
        (li[32] if len(li[32])>0 else '-')+'\n'+price_jn.get('A9','--'),  # 商务座
        (li[31] if len(li[31])>0 else '-')+'\n'+price_jn.get('M','--'),  # 一等座
        (li[30] if len(li[30])>0 else '-')+'\n'+price_jn.get('O','--'),  # 二等座
        (li[22] if len(li[22])>0 else '-')+'\n'+price_jn.get('A6','--'),  # 高级软卧
        (li[23] if len(li[23])>0 else '-')+'\n'+price_jn.get('A4','--'),  # 软卧
        (li[24] if len(li[24])>0 else '-')+'\n'+price_jn.get('F','--'),  # 动卧
        (li[28] if len(li[28])>0 else '-')+'\n'+price_jn.get('A3','--'),  # 硬卧
        (li[27] if len(li[27])>0 else '-')+'\n'+'--',  # 软座
        (li[26] if len(li[26])>0 else '-')+'\n'+price_jn.get('A1','--'),  # 硬座
        (li[29] if len(li[29])>0 else '-')+'\n'+price_jn.get('WZ','--'),  # 无座
    ])
print(pt)