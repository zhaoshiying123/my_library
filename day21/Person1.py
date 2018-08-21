# @Time:2018/8/21 10:13
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'Sean'
class Person:
    role = 'person'  # 人的角色分类

    def __init__(self):
        self.name =''  # 每个人都有一个自己的昵称
        self.attack = 50  # 定义初始攻击力
        self.hp = 1000  # 定义初始血量1000

    def walk(self):  # 人都可以走路，属于一种行为特性，也称为动态属性
        print('%d年级的身高%d厘米的%d岁的%s在走路' % (self.grade, self.height, self.age, self.name))

    def attacking(self, dog):  # 定义人类攻击的方法
        dog.hp = dog.hp - self.attack
