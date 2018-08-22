# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/22 18:41
# @Author : 'Sean'
# @File   : Animal.py
import random

class Animal:
    def __init__(self):
        self.x = random.randint(0,9)
        self.y = random.randint(0,9)
        self.name = ''

class Cat(Animal):
    power = 100
    def move(self):
        self.x += random.choices([-1, -2, 1, 2])[0]
        self.y += random.choices([-1, -2, 1, 2])[0]
        if self.x < 0 :
            self.x += 10
        if self.x > 9 :
            self.x -= 10
        if self.y < 0 :
            self.y += 10
        if self.y > 9 :
            self.y -= 10
        Cat.power -= 1
    def eat(self):
        Cat.power +=10
        if Cat.power > 100:
            Cat.power = 100

class Mouse(Animal):
    def move(self):
        self.x += random.choices([-1, 1])[0]
        self.y += random.choices([-1, 1])[0]
        if self.x < 0 :
            self.x += 10
        if self.x > 9 :
            self.x -= 10
        if self.y < 0 :
            self.y += 10
        if self.y > 9 :
            self.y -= 10

cat = Cat()
cat.name = 'Tom'

mice = []
for i in range(10):
    mouse = Mouse()
    mouse.name = 'Jerry'+ str(i)
    mice.append(mouse)

while cat.power and len(mice):
    print(cat.power, len(mice))
    cat.move()
    for j in mice:
        j.move()
        if cat.x == j.x and cat.y ==j.y:
            print('%s抓到了%s' %(cat.name,j.name))
            cat.eat()
            mice.remove(j)

if cat.power==0:
    print('猫没有力气了')
if len(mice)==0:
    print('老鼠被抓光了')