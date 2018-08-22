# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/22 10:52
# @Author : 'Sean'
# @File   : Cat.py
import random


class Cat():
    def __init__(self):
        self.x = random.randint(0,9)
        self.y = random.randint(0,9)
        self.power = 500
    def move(self):
        self.x += random.choices([-1, -2, 1, 2])[0]
        self.y += random.choices([-1, -2, 1, 2])[0]
        self.x %= 10
        self.y %= 10
        self.power -= 1
    def eat(self):
        self.power += 10
        if self.power > 100 :
            self.power = 100