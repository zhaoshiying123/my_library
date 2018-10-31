# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/31 15:06
# @Author : 'Sean'
# @File   : For.py
li = [1,2,3,4,5,6,7,8,9]
li1 = []
for x in li:
    li1.append(x * 2)
print(li1)
#推导式：
print([x*2 for x in li])

#函数+推导式：
def mul(x):
    return x * 2
print([mul(y) for y in li])

list1 = [1,2,3,4,5]
list2 = []
dt = {}
for x in list1:
    dt[x] = x ** 2
    list2.append(dt)
    dt = {}
print(list2)

list3 = []
for x in list1:
    d = { x : x**2}
    list3.append(d)
print(list3)

#推导式：
print([{x:x**2} for x in list1])

list4  = [1,2,3,4,5,6,7,8,9]
list5 = []
for x in list4:
    if x%2 == 1:
        list5.append(x*2)
print(list5)

#推导式：
print([x*2 for x in list4 if x%2 == 1])

# 推导式
# print([(x*y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y >7 if y !=8 ])

for x in range(10):
    if x % 2:
        if x > 3:
            for y in range(10):
                if y > 7:
                    if y != 8:
                        print(x * y)

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,1,1],[2,2,2],[3,3,3]]
# for a,b in zip(a,b):
#     print(a,b)
#     print(list(zip(a,b)))
#     for x,y in zip(a,b):
#         print(x,y)

print( [(x*y) for a,b in zip(a,b) for x,y in zip(a,b)] )