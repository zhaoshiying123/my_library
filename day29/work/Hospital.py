# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/31 18:48
# @Author : 'Sean'
# @File   : Hospital.py
'''
Usage:
    aa <city>
'''
import requests
from docopt import docopt
args = docopt(__doc__)
city = args['<city>']
url = 'https://raw.githubusercontent.com/open-power-workgroup/' \
      'Hospital/master/resource/API_resource/hospital_list.json'
re = requests.get(url)
print(re.status_code)
jn = re.json()[city]
for k,v in jn.items():
    print(k)