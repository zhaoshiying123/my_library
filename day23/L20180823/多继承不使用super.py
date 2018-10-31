# @Time :2018/8/23 002314:26
# @Author :Alex
# @File  :多继承不使用super.py


class Base(object):
    def __init__(self):
        print('我是Base父类构造器')

'''
object 可以改成父类，也可以不改
'''
class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('我是子类A的构造器')

class B(Base):
    name = 'abc'
    def __init__(self):
        Base.__init__(self)
        print('我是子类B的构造器')

'''
如果想一次继承多个类，那么在()里面使用逗号隔开即可
构造器的作用，是用来创建实例对象，如果同时继承多个类的时候，只会调用第一个类的构造器来创建实例（深度调用）
'''
class C(A, B):
    pass

'''
调用init,就会创建实例，并且父类被调用多次
'''
class D(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('我是子类D的构造器')

'''
只会输出我是Base父类构造器和我是子类A的构造器，而不会输出B，
但是B类的属性和方法依然可以继承
'''
c = C()
# print(c.name)
# print(C.__bases__)
# print(C.__dict__)
# d = D()

