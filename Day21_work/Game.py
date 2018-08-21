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
list2 = []
for i in range(10):
    Jerry = Mouse(10)
    pos = [random.randint(1, 10), random.randint(1, 10)]
    if Tom.position==pos:
        Jerry.count -= 1
        continue
    list1.append(pos)
print(list1)

def move():
    global a,b
    x1 = random.choices([1,2,-1,-2])[0]
    y1 = random.choices([1,2,-1,-2])[0]
    print('=======',x1,y1)
    Tom.position[0] += x1
    Tom.position[1] += y1
    if Tom.position[0]==11:
        Tom.position[0] = 1
    if Tom.position[0]==12:
        Tom.position[0] = 2
    if Tom.position[0]==0:
        Tom.position[0] = 10
    if Tom.position[0]==-1:
        Tom.position[0] = 9

    if Tom.position[1]==11:
        Tom.position[1] = 1
    if Tom.position[1]==12:
        Tom.position[1] = 2
    if Tom.position[1]==0:
        Tom.position[1] = 10
    if Tom.position[1]==-1:
        Tom.position[1] = 9
    print(Tom.position)
    a1 = random.choices([1, 2, -1, -2])[0]
    b1 = random.choices([1, 2, -1, -2])[0]
    for p in list1:
        p[0] += a1
        p[1] += b1
        if p[0] == 11:
           p[0] = 1
        if p[0] == 12:
           p[0] = 2
        if p[0] == 0:
            p[0] = 10
        if p[0] == -1:
            p[0] = 9

        if p[1] == 11:
            p[1] = 1
        if p[1] == 12:
            p[1] = 2
        if p[1] == 0:
            p[1] = 10
        if p[1] == -1:
            p[1] = 9
    print(list1)

while(Tom.hp and Jerry.count):
    move()
    Tom.hp -= 1
    for q in list1:
        # Tom.position = [8,4]
        if (Tom.position==q):
            print('抓到一只老鼠',q)
            list1.remove(q)
            Jerry.count -= 1
            Tom.hp += 10
            if Tom.hp>100:
                Tom.hp = 100
if Tom.hp==0:
    print('Tom没有体力了')
if Jerry.count==0:
    print('老鼠被抓完了')