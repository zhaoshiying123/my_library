# @Time :2018/8/22 002216:34
# @Author :Alex
# @File  :人类.py

'''
父类：也称为基类
子类：也称为派生类
父类一般里面的属性和方法比子类要少
子类属于父类，但是父类不一定属于子类
'''

class People:
    sex = ''  # 性别
    name = ''  # 名字
    age = 0  # 年龄

    # 人类都得吃东西
    def eat(self):
        print('我是人类,我的性别是%s,我今年%d岁，我叫%s，我得吃东西' % (self.sex, self.age, self.name))


'''
class A(B)， A类继承B类
A类拥有B类里面的方法和属性
'''


class Student(People):
    def readbook(self):
        print("我需要阅读")

class Teacher(People):
    pass

stu = Student()
stu.name = '小明'
stu.age = 20
stu.sex = '男'
stu.eat()

ter = Teacher()
ter.name = '小红'
ter.age = 30
ter.sex = '女'
ter.eat()

print('学生是否属于Student实例：',isinstance(stu, Student))
print('学生是否属于Teacher实例：',isinstance(stu, Teacher))
print('学生是否属于People实例：',isinstance(stu, People))

peo = People()
print('人类是否属于Student实例：',isinstance(peo, Student))
print('人类是否属于Teacher实例：',isinstance(peo, Teacher))
print('人类是否属于People实例：',isinstance(peo, People))

