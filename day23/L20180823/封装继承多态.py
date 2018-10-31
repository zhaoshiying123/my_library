# @Time :2018/8/23 00238:44
# @Author :Alex
# @File  :封装继承多态.py


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: linghanchujian

# python类
# 类模板

class Person(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

class Child(Person):                # Child 继承 Person
    def __init__(self,name,sex,mother,father):
        # self.name = name
        # self.sex = sex
        # Person.__init__
        super(Child, self).__init__(name,sex)
        self.mother = mother

        self.father = father


May = Child("May","female","April","June")
print(May.name,May.sex,May.mother,May.father)
