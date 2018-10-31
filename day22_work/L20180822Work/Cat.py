# @Time :2018/8/22 002210:18
# @Author :Alex
# @File  :Cat.py
import random
from L20180822Work.Animal import Animal

# 使用猫继承动物类，自动继承父类的x、y、name属性
class Cat(Animal):
    # def __init__(self):
    #     # 定义猫初始化时候的体力值为100
    #     self.power = 100

    power = 100

    def move(self):
        b = True
        # random.choice()表示从一个集合里面随机取出一个元素
        # 猫一次移动可以随机移动两步或者一步，修改横纵坐标
        self.x = self.x + random.choice([-1, -2, 1, 2])
        self.y = self.y + random.choice([-1, -2, 1, 2])

        # 如果走完之后超过横坐标最右边，那么减10回到同行的另一侧，类似贪吃蛇
        # 如果走完之后超过横坐标最左边，那么加10回到同行的另一侧，类似贪吃蛇
        if self.x < 0:
            self.x += 10
        elif self.x > 9:
            self.x -= 10
        else:
            pass

        # 如果走完之后超过纵坐标最上边，那么减10回到同行的另一侧，类似贪吃蛇
        # 如果走完之后超过纵坐标最下边，那么加10回到同行的另一侧，类似贪吃蛇
        if self.y < 0:
            self.y += 10
        elif self.y > 9:
            self.y -= 10
        else:
            pass
        self.power -= 1

    def eatMouse(self):
        self.power += 10
        if self.power > 100:
            self.power = 100


