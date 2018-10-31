# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/24 14:54
# @Author : 'Sean'
# @File   : 私有变量的使用.py
class Student:
    name = 'xiaoming'
    age = 18
    __sex = '男'
    __address = '广东深圳'
    def getAddress(self):
        return self.__address
    def updateAddr(self,addr):
        if '广东' not in addr:
            print('输入地址有误')
        else:
            self.__address = addr
    def isAddrInsz(self,addr):
        if '深圳' in addr:
            print('确实在深圳')
        else:
            print('地址有误')

class College_Studdent(Student):
    pass

stu = Student()
stu.name = '小明'
stu.age = 20

# print(stu.__sex)
# print(stu.__address)

# addr = stu.getAddress()
# if addr == '广东深圳':
#     stu.updateAddr('广东深圳aaa')
# print(stu.getAddress())

stu.isAddrInsz(stu.getAddress())
stu.updateAddr('广东深圳aaa')
print(stu.getAddress())

cs = College_Studdent()
print(cs.name)
print(cs.age)

# print(cs.__sex)
# print(cs.__address)

