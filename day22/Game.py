# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/22 11:01
# @Author : 'Sean'
# @File   : Game.py
from day22 import Cat,Mouse


Tom = Cat.Cat()

list1 = []
for i in range(10):
    Jerry = Mouse.Mouse()
    list1.append(Jerry)

while True:
    list2 = []
    Tom.move()
    print('猫：',(Tom.x,Tom.y))
    for j in list1:
        j.move()
        list2.append((j.x,j.y))
        if Tom.x==j.x and Tom.y==j.y:
            print('抓到一只老鼠')
            list1.remove(j)
            Tom.eat()
    print(list2)
    if Tom.power==0:
        print('猫没力气了')
        break
    if len(list1)==0:
        print('老鼠被抓光了')
        break