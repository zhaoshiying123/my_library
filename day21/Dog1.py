# @Time:2018/8/21 10:14
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'Sean'

class Dog:
    role = 'dog'  # 定义一个狗的角色

    def __init__(self):
        self.name = ''  # 每只狗都有自己的名字
        self.attack = 80  # 每只狗都有自己的攻击力
        self.hp = 500  # 每只狗都有自己的血量

    def bite(self, person):
        person.hp = person.hp - self.attack
