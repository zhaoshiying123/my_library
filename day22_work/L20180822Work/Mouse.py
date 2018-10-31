# @Time :2018/8/22 002210:18
# @Author :Alex
# @File  :Mouse.py
import random
from L20180822Work.Animal import Animal


class Mouse(Animal):
    # def __init__(self):
    #     pass

    def move(self):
        # random.choice()表示从一个集合里面随机取出一个元素
        # 老鼠一次移动只能随机移动一步，修改横纵坐标
        self.x = self.x + random.choice([-1, 1])
        self.y = self.y + random.choice([-1, 1])

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
