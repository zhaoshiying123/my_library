# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/31 16:21
# @Author : 'Sean'
# @File   : Input.py
'''
Usage:
       GetTrainTicket <beg> <end> <date>
'''
from Train.Station import stations
from docopt import docopt

arguments = docopt(__doc__)
beg = stations[arguments['<beg>']]
end = stations[arguments['<end>']]
date = arguments['<date>']