# @Time :2018/8/23 002310:55
# @Author :Alex
# @File  :单继承不带参数.py


class BaseMode(object):
    name = 'baseMode'
    def __init__(self):
        print('我是基类的构造器')

# 如果继承父类以后，没有写__init__方法，那么默认继承父类的__init__和属性、以及其他方法
class A(BaseMode):
    pass

# 默认会调用父类的构造器
a = A()

# 如果继承父类以后，自己又写了__init__方法，那么将不再继承父类的__init__方法，但是属性和其他方法依旧继承
class B(BaseMode):
    def __init__(self):
        print('我是B类的构造器')

# 自己写了__init__之后，不再继承父类的__init__，但是属性和其他方法依然继承
b = B()
print(b.name)

# 使用super继承父类的__init__方法
class C(BaseMode):
    def __init__(self):
        super(C, self).__init__()

c = C()

#使用父类.__init__(self)继承
class D(BaseMode):
    def __init__(self):
        BaseMode.__init__(self)

d = D()

