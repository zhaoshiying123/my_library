# @Time :2018/8/23 002315:04
# @Author :Alex
# @File  :多继承练习.py

"""
使用super()的时候，并不是一定需要关联到某个直接的父类上面，才可以继承；
一次继承多个类，本质上就是先用B继承A，然后用C继承B，然后用D继承C
如下：
"""


class A(object):
    def __init__(self):
        print('我是方法A')

class B(object):
    def __init__(self):
        super().__init__()
        print('我是方法B')

class C(object):
    def __init__(self):
        super().__init__()
        print('我是方法C')

# 一次继承多个类，本质上就是先用B继承A，然后用C继承B，然后用D继承C
class D(C, B, A):
    pass

# class B(A)
# class C(B)
# class D(C)
d = D()

class E(C, B, A):
    def __init__(self):
        super(E, self).__init__()
# e = E()