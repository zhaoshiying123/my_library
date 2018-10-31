# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/21 17:02
# @Author : 'Sean'
# @File   : Day21_work.py
import random
class Cat:
    position = [random.randint(1, 10),random.randint(1, 10)]
    def __init__(self,hp):
        self.hp = hp

class Mouse:
    def __init__(self,count):
        self.count = count


Tom = Cat(10000)
print(Tom.position)

list1 = []

for i in range(10):
    Jerry = Mouse(10)
    pos = [random.randint(1, 10), random.randint(1, 10)]
    if Tom.position==pos:
        Jerry.count -= 1
        continue
    list1.append(pos)
print(list1)

def border(p0,p1):
    if p0 > 10:
        p0 -= 10
    if p0 < 1:
        p0 += 10
    if p1 > 10:
        p1 -= 10
    if p1 < 1:
        p1 += 10
    return p0,p1

def move(tp0,tp1):
    x1 = random.choices([1,2,-1,-2])[0]
    y1 = random.choices([1,2,-1,-2])[0]
    tp0 += x1
    tp1 += y1
    tp0,tp1=border(tp0,tp1)
    return [tp0,tp0]
while(Tom.hp and Jerry.count):
    list2 = []
    Tom.position = move(Tom.position[0],Tom.position[1])
    print(Tom.position)
    for p in list1:
        y = move(p[0], p[1])
        list2.append(y)
    print(list2)
    Tom.hp -= 1
    for q in list2:
        if (Tom.position==q):
            print('抓到一只老鼠',q)
            list2.remove(q)
            Jerry.count -= 1
            Tom.hp += 10
            if Tom.hp>100:
                Tom.hp = 100
if Tom.hp==0:
    print('Tom没有体力了')
if Jerry.count==0:
    print('老鼠被抓完了')