# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/23 15:35
# @Author : 'Sean'
# @File   : base.py
class A(object):
    def __init__(self):
        print('我是类A')
class B(object):
    def __init__(self):
        A.__init__(self)
        print('我是类B')
class C(object):
    def __init__(self):
        B.__init__(self)
        print('我是类C')

class D(B,A,C):
    pass
d = D()