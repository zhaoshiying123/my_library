# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/22 10:59
# @Author : 'Sean'
# @File   : Mouse.py
import random

class Mouse():
    def __init__(self):
        self.x = random.randint(0,9)
        self.y = random.randint(0,9)
    def move(self):
        self.x += random.choices([-1, 1])[0]
        self.y += random.choices([-1, 1])[0]
        self.x %= 10
        self.y %= 10