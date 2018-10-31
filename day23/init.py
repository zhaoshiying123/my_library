# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/23 11:27
# @Author : 'Sean'
# @File   : init.py
class Base(object):
    name = 'BaseMode'
    def __init__(self):
        print('我是基类')
'''
直接继承基类的init、属性和其他方法
'''
class A0(Base):
    pass
'''
覆盖init
'''
class A1(Base):
    def __init__(self):
        print('我是子类A1')
# class B(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('我是子类B')
'''
继承基类的init并添加
'''
class C(Base):
    def __init__(self):
        super(C,self).__init__()
        print('我是子类C')

a0 = A0()
a1 = A1()
print(a1.name)
# b = B()
c = C()