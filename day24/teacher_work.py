# @Time :2018/8/27 002711:39
# @Author :Alex
# @File  :Work.py

# 定义父类的Person


class Person(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


#定义男人类，继承人类
class Man(Person):
    def __init__(self, name, age, height, weight, hx, money, play, work, whitehair):
        super().__init__(name, age, height, weight, hx, money, play, work, whitehair)
        self.hx = hx
        print('他有短头发')


#定义女人类，继承人类
class Woman(Person):
    def __init__(self, name, age, height, weight, hx, money, play, work, whitehair):
        super().__init__(name, age, height, weight, hx, money, play, work, whitehair)
        # self.money = money
        # self.hx = hx
        # self.play = play
        # self.work = work
        # self.whitehair = whitehair
        print('他有长头发')


# 定义一个小孩，继承人类
class Child(Person):
    def __init__(self, name, age, height, weight, hx, money, play, work, whitehair):
        super(Child, self).__init__(name, age, height, weight)
        self.play = play
        print('我是个孩子')


# 定义一个大人，继承人类
class Adult(Person):
    def __init__(self, name, age, height, weight, hx, money, play, work, whitehair):
        super(Adult, self).__init__(name, age, height, weight)
        self.work = work
        print('我是个大人')


# 定义一个老人，继承人类
class Older(Person):
    def __init__(self, name, age, height, weight, hx, money, play, work, whitehair):
        super(Older, self).__init__(name, age, height, weight)
        self.whitehair = whitehair
        print('我是个老人')

# 定义一个集合，集合里面第一个表示性别，第二个表示年龄，如果年龄小于18岁那么是个孩子，如果18到50那么是大人，否则是老人


classParam = ['女', 16]

# 定义一个经理
sex = classParam[0]
age = classParam[1]


class Manager(Man if sex == '男' else Woman, Child if age < 18 else Adult if 17 < age <50 else Older):
    def __init__(self, sex, name, age, height, weight, hx, money, play, work, whitehair):
        super(Manager, self).__init__(name, age, height, weight, hx, money, play, work, whitehair)
        self.money = money
        # if sex == '男':
        #     super(Manager, self).__init__(name, age, height, weight, hx, work)
        # else:
        #     super(Manager, self).__init__(name, age, height, weight, money)


    def buyCar(self, Car):
        # 称谓
        who = ''
        # 发型
        hair = ''
        if sex == '男':
            hair = '短头发'
            if age < 18:
                who = '大男孩'
            elif 17 < age < 50:
                who = '大男人'
            else:
                who = '老男人'
        else:
            hair = '长头发'
            if age < 18:
                who = '大女孩'
            elif 17 < age < 50:
                who = '大女人'
            else:
                who = '老女人'

        print('经理是一个%s经理，也是%s，我有%s，他买了一辆%s车，车的颜色是%s，车的价格是：%d万' % (sex, who, hair, Car.name, Car.color, Car.price))



# 车的基本定义
class Car(object):
    def __init__(self, color, price):
        self.color = color
        self.price = price


# 奔驰
class Benz(Car):
    def __init__(self, color, price):
        super(Benz, self).__init__(color, price)
        self.name = '奔驰'
        print('我是一辆奔驰车')


# 宝马
class Bmw(Car):
    def __init__(self, color, price):
        super(Bmw, self).__init__(color, price)
        self.name = '宝马'
        print('我是一辆宝马车')


# 奥迪
class Audi(Car):
    def __init__(self, color, price):
        super(Audi, self).__init__(color, price)
        self.name = '奥迪'
        print('我是一辆奥迪车')


ma = Manager('女', '小明', 20, 150, 280, '胡子', '有钱', '玩具', '工作', '白头发')

bz = Audi('红色', 50)

ma.buyCar(bz)
print(ma.money)




print(5 if 5>6 else (6 if 3>2 else 5))