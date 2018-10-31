# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/24 16:12
# @Author : 'Sean'
# @File   : day24_work.py
class People(object):
    def __init__(self,age,height,weight,name):
        self.age = age
        self.height = height
        self.weight  = weight
        self.name = name

class Man(People):
    hair = '短头发'
class Woman(People):
    hair = '长头发'

class Young(People):
    boy = '大男孩'
    girl = '小女人'
class Adult(People):
    man = '大男人'
    woman = '大女人'
class Old(People):
    man = '老男人'
    woman = '老女人'

class Car(object):
    def __init__(self,color,price):
        self.color = color
        self.price = price
class BMW(Car):
    name = '宝马'
    def __init__(self,color,price):
        Car.__init__(self,color,price)
class BC(Car):
    name = '奔驰'
    def __init__(self,color,price):
        Car.__init__(self,color,price)
class AD(Car):
    name = '奥迪'
    def __init__(self,color,price):
        Car.__init__(self,color,price)

class Manager(Adult):
    def buy_car(self):
        print('经理是一个%s,他有%s,他买了一辆%s元的%s%s' %(Adult.man,Man.hair,bmw.price,bmw.color,BMW.name))

bmw = BMW('灰色','60w')
manager = Manager(30,180,70,'张三')
manager.buy_car()



