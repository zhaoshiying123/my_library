# @Time :2018/8/23 002311:03
# @Author :Alex
# @File  :单继承带参数.py


# 这是一个需要带参数实例化的父类
class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('我是基类的构造器')
"""
如果子类自己要写__init__方法，又想继承父类的构造器，有两种方式
1、父类.__init__(self,参数)
2、super(子类, self).__init__(参数)
"""
'''
object可以改成基类，也可以不改
'''
class Child(People):
    def __init__(self, name, age, height):
        People.__init__(self, name, age)
        self.height = height
        print('我是个小孩，我的名字是%s,我的年龄是：%d,我的身高是%d' % (self.name, self.age, self.height))

# child = Child('小明', 5, 30)

'''
object必须改成基类
'''
class Child2(People):
    def __init__(self, name, age, height):
        super(Child2, self).__init__(name, age)
        self.height = height
        print('我是个小孩，我的名字是%s,我的年龄是：%d,我的身高是%d' % (self.name, self.age, self.height))

child = Child2('小明', 6, 40)
