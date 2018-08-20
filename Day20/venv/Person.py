# @Time :2018/8/20 002016:04
# @Author :Alex
# @File  :Person.py

"""
定义一个人的类
"""


class Person:
    role = 'person'  # 人的角色分类

    def __init__(self, name, age, height):
        self.name = name  # 每个人都有一个自己的昵称
        self.age = age  # 每个人都有自己的年龄
        self.height = height  # 每个人都有自己的身高
        self.grade = 0  # 定义这个人的年级

    def fight(self):  # 人都可以走路，属于一种行为特性，也称为动态属性
        print('%d年级的身高%d厘米的%d岁的%s在打'%(self.grade, self.height, self.age, self.name))


class Dog:
    role = 'dog'

    def __init__(self,name,age,height,color):
        self.name = name
        self.age = age
        self.height = height
        self.color = color
    def bite(self):
        print('{}的身高{}cm的{}岁的{}在咬'.format(self.color,self.height,self.age,self.name))
'''
属性引用(类名.属性)
'''
print(Person.role)
print(Person.fight)
print(Dog.role)
print(Dog.bite)


'''
实例化(类名(参数)) 实例化的过程就是  类 → 对象 的过程
默认是无参的构造函数，不需要参数
有参的构造函数使用 __init__来创建

person = Person() 类名()的调用就等效于执行了 Person.__init__()
__init__() 执行完就会返回一个类似字典的结构，里面包含人类所属的 一些属性 和  方法
可以变相理解为：person = {'name':'xiaoming', 'walk':walk, 'role':'person'}
'''
person = Person('小明', 20, 178)
dog = Dog('小黑',5,50,'黑色')
# 对象.属性 = 值，可以对对象的属性进行修改
person.grade = 6
person.age = 25
# 调用对象的方法
person.fight()
dog.bite()
