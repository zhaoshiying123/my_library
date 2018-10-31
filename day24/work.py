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
    def __init__(self,age,height,weight,name,beard,sense):
        super(Man, self).__init__(age,height,weight,name)
        self.beard = beard
class Woman(People):
    def __init__(self,age,height,weight,name,beard,sense):
        super(Woman, self).__init__(age,height,weight,name)
        self.sense = sense

class Child(People):
    def __init__(self,age,height,weight,name):
        super(Child, self).__init__(age,height,weight,name)

class Adult(People):
    def __init__(self,age,height,weight,name):
        super(Adult, self).__init__(age,height,weight,name)

class Older(People):
    def __init__(self,age,height,weight,name):
        super(Older, self).__init__(age,height,weight,name)

class Car(object):
    def __init__(self,color,price):
        self.color = color
        self.price = price
class BMW(Car):
    def __init__(self,color,price):
        super(BMW, self).__init__(color, price)
        self.name = '宝马'
class Benz(Car):
    def __init__(self,color,price):
        super(Benz, self).__init__(color, price)
        self.name = '奔驰'
class Audi(Car):
    def __init__(self,color,price):
        super(Audi, self).__init__(color, price)
        self.name = '奥迪'

classParam = ['女',17]
sex = classParam[0]
age = classParam[1]
class Manager(Man if sex == '男' else Woman,Child if age<18 else Adult if 17<age<50 else Older ):
    def __init__(self,age,height,weight,name,beard,sense):
        super(Manager, self).__init__(age,height,weight,name,beard,sense)
    '''
    继承Car self不能掉
    '''
    def buy_car(self,Car):
        if sex == '男':
            hair = '短头发'
            if age < 18:
                who = '大男孩'
            elif 17<age<50:
                who = '大男人'
            else:
                who = '老男人'
        else:
            hair = '长头发'
            if age < 18:
                who = '小女孩'
            elif 17 < age < 50:
                who = '大女人'
            else:
                who = '老女人'
        print('经理是一个%s,他有%s,他买了一辆%s万元的%s%s' %(who,hair,Car.price,Car.color,Car.name))

bmw = BMW('灰色','60')
manager = Manager(30,180,70,'张三','b','s')
manager.buy_car(bmw)



