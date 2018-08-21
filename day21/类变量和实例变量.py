# @Time :2018/8/21 002111:12
# @Author :Alex
# @File  :类变量和实例变量.py


class A:
    # 在类里面，但是在方法外面，叫做类变量，也叫静态变量
    a = 10
    b = 20

    def __init__(self):
        # c和d就是定义的实例变量，在方法内部，也叫非静态变量
        self.c = 30
        self.d = 40

    def add(self):
        print('使用self后：%d + %d + %d + %d=%d' % (self.a, self.b, self.c, self.d, self.a + self.b + self.c + self.d))
        print('使用类变量后：%d + %d + %d + %d=%d' % (A.a, A.b, self.c, self.d, A.a + A.b + self.c + self.d))


# 修改的是类变量，也是静态变量，修改之后，所有实例里面的这个变量值都会修改
A.a = 80
A.b = 100

aa = A()
# 如果使用实例.类变量 修改之后，该变量含义改变，变成实例变量
aa.a = 100
aa.c = 50
aa.add()

aa1 = A()
aa1.c = 90
aa1.add()
