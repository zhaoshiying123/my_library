# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/24 14:36
# @Author : 'Sean'
# @File   : 双下划线.py
class A(object):
    def __init__(self):
        self.name = '张三'
    def __privateFunc(self):
        print('不会被继承的私有方法')
    def publicFunc(self):
        print('可以被继承公共方法')
    def _protectedFunc(self):
        print('可以被继承的受保护方法')
    def getPrivateFunc(self):
        print('调用私有方法')
        self.__privateFunc()

class B(A):
    pass

a = A()
b = B()

# a.getPrivateFunc()
# a._protectedFunc()
# a.publicFunc()
# a.__privateFunc()

b.getPrivateFunc()
b._protectedFunc()
b.publicFunc()
# b.__privateFunc()
