# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/31 17:09
# @Author : 'Sean'
# @File   : Docopt.py
'''
Usage:
    aa <name> <cardID>
'''
from docopt import docopt
arguments = docopt(__doc__)
name = arguments['<name>']
cardID = arguments['<cardID>']
print(arguments)
print(name,cardID)
