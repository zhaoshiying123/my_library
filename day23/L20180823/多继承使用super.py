# @Time :2018/8/23 002314:46
# @Author :Alex
# @File  :多继承使用super.py


"""
1、如果使用 父类.__init__()的方式，那么使用深度调用
2、如果使用 super().init()的方式，那么使用广度调用

深度指的是父子类的层级，比如 base、A、C三者的关系
广度指的是同一层级的扩展量，比如A、B之间的关系
"""


class Base(object):
    def __init__(self):
        print('我是Base父类构造器')

class A(Base):
    def __init__(self):
        # Base.__init__(self)
        super(A, self).__init__()
        print('我是子类A的构造器')

class B(Base):
    def __init__(self):
        # Base.__init__(self)
        super(B, self).__init__()
        print('我是子类B的构造器')

class B1(Base):
    def __init__(self):
        # Base.__init__(self)
        super(B1, self).__init__()
        print('我是子类B1的构造器')

'''
如果想一次继承多个类，那么在()里面使用逗号隔开即可
构造器的作用，是用来创建实例对象，如果同时继承多个类的时候，
会从右往左调用类的构造器来创建实例，并且基类只会第一次调用(广度调用）
'''

class C(A, B, B1):
    pass

class D(A, B, B1):
    def __init__(self):
        # A.__init__(self)
        # B.__init__(self)
        # super(D, self).__init__()
        super().__init__()
        print('我是子类D的构造器')

# 只会输出我是Base父类构造器和我是子类A的构造器，而不会输出B，但是B类的属性和方法依然可以继承
# c = C()
# print(c.name)

d = D()