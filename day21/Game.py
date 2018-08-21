# @Time:2018/8/21 10:14
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# __author__ = 'Sean'

from day21 import Person1, Dog1

dog = Dog1.Dog()
dog.name = '小黑'
per = Person1.Person()
per.name = '小明'
dog.bite(per)
print(per.hp)
per.attacking(dog)
print(dog.hp)
