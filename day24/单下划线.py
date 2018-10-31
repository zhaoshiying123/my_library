# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/24 12:00
# @Author : 'Sean'
# @File   : 单下划线.
_sex = '男'
height = 150

class AA:
    name = 'abc'
    age = 20
    _address = '广东深圳'

    def __init__(self,_phone):
        self._phone = _phone
        print('%s孩子' %_sex)

class _BB:
    pass


