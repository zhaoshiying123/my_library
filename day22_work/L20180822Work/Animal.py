# @Time :2018/8/23 00239:42
# @Author :Alex
# @File  :Animal.py


"""
Animal作为父类，后面可以加()，也可以不加

Animal后面的() 里面可以写object类、也可以不写
如果写了object表示显示继承，如果没写，表示隐式继承
"""
# 父类里面开始定义公共的特性属性
import random


class Animal(object):
    def __init__(self, name):
        self.name = name
        # 定义猫出生的时候横坐标地址
        self.x = random.randint(0, 9)
        # 定义猫出生的时候纵坐标地址
        self.y = random.randint(0, 9)

        print('==================我是子类实例化调用的==================')
