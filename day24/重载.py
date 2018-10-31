# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/24 19:58
# @Author : 'Sean'
# @File   : 重载.py
def test(x,y,z,**kwargs):
#print里面不用写**
    print(x,y,z,kwargs)
test(1,2,3,a=4,b=5)

def test1(x,y,z):
    print(x,y,z)

xx = [1,2,3]
yy = {'a','c','b'}
zz = {'x':1,'z':2,'y':3}
'''
将集合传进去，需要先拆包
'''
test1(*xx)
test1(*yy)
'''
使用字典的**拆包传递数据，要保证字典里面的key值和参数名一样
'''
test1(**zz)