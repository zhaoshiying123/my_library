# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time   : 2018/8/31 14:31
# @Author : 'Sean'
# @File   : Zip.py
'''
从一个或多个迭代器里面取出元素组合成一个新的迭代器
zip迭代器分别从a和b里面抽取元素，内部组成元组
'''
#一个集合
a = [1,2,3]
x = zip(a)
print(x)
print(list(x))

#两个集合
a = [1,2,3]
b = [4,5,6]
y = list(zip(a,b))
print(y)

print(dict(zip(a,b)))
#上面的代码等效于
print(dict(y))

#多个集合
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = [5,5,5]
print(list(zip(a,b,c,d)))

#长度不一致时，以最短长度的集合为标准
a = [1,2,3]
b = [4,5,6,6]
c = [7,8,9,10,11]
print(list(zip(a,b,c)))

#zip函数的应用
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,1,1],[2,2,2],[3,3,3]]
print([(x*y) for m,n in zip(a,b) for x,y in zip(m,n)])

#zip*zipped 函数：zip的逆过程，将zip对象变成组合之前的数据
i = [(1, 4, 7, 5), (2, 5, 8, 5), (3, 6, 9, 5)]
#解压
print(zip(*i))
print(list(zip(*i)))

