# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/23 15:26
# @Author : 'Sean'
# @File   : super.py
class A(object):
    def __init__(self):
        print('我是类A')
class B(object):
    def __init__(self):
        super(B, self).__init__()
        print('我是类B')
class C(object):
    def __init__(self):
        super(C, self).__init__()
        print('我是类C')
'''
深度遍历
'''
class D(C,B,A):
    pass
d = D()