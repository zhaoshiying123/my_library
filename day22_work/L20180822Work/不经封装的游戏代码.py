# @Time :2018/8/23 002310:32
# @Author :Alex
# @File  :不经封装的游戏代码.py


"""
游戏编程：按以下要求定义一个猫类和老鼠类并尝试编写游戏

假设游戏场景为范围（x,y）为0<=x<=10,0<=y<=10
游戏生成1只猫和10条老鼠
它们的移动方向均随机，每次移动左右选择一次，上下选择一次，也就是必须横向走一次，纵向走一次
猫的最大移动能力为2（它可以随机选择1还是2移动），老鼠儿的最大移动能力是1
当移动到场景边缘，自动向反方向移动
猫初始化体力为100（上限）
猫每移动一次，体力消耗1
当猫和老鼠坐标重叠，猫吃掉老鼠，猫体力增加10
老鼠暂不计算体力
当猫体力值为0（挂掉）或者老鼠儿的数量为0游戏结束
"""
from day22_work.L20180822Work.Cat import Cat
from day22_work.L20180822Work.Mouse import Mouse
import random
"""
这就是面向过程的编程思想，代码未经过面向对象思想的封装处理
"""

# 定义一个猫
tom = Cat('tom')

# 定义10只老鼠
mouses = []


for x in range(10):
    mouse = Mouse('kit'+str(x))
    mouses.append(mouse)

# 猫和老鼠开始移动
while True:
    if tom.power == 0:
        print('猫已经累死了...')
        break
    if len(mouses) == 0:
        print('老鼠被抓完了...')
        break
    # 猫移动一次
    # random.choice()表示从一个集合里面随机取出一个元素
    # 猫一次移动可以随机移动两步或者一步，修改横纵坐标
    tom.x = tom.x + random.choice([-1, -2, 1, 2])
    tom.y = tom.y + random.choice([-1, -2, 1, 2])

    # 如果走完之后超过横坐标最右边，那么减10回到同行的另一侧，类似贪吃蛇
    # 如果走完之后超过横坐标最左边，那么加10回到同行的另一侧，类似贪吃蛇
    if tom.x < 0:
        tom.x += 10
    elif tom.x > 9:
        tom.x -= 10
    else:
        pass

    # 如果走完之后超过纵坐标最上边，那么减10回到同行的另一侧，类似贪吃蛇
    # 如果走完之后超过纵坐标最下边，那么加10回到同行的另一侧，类似贪吃蛇
    if tom.y < 0:
        tom.y += 10
    elif tom.y > 9:
        tom.y -= 10
    else:
        pass
        tom.power -= 1

    # 10只老鼠开始移动
    for mos in mouses:

        # random.choice()表示从一个集合里面随机取出一个元素
        # 老鼠一次移动只能随机移动一步，修改横纵坐标
        mos.x = mos.x + random.choice([-1, 1])
        mos.y = mos.y + random.choice([-1, 1])

        # 如果走完之后超过横坐标最右边，那么减10回到同行的另一侧，类似贪吃蛇
        # 如果走完之后超过横坐标最左边，那么加10回到同行的另一侧，类似贪吃蛇
        if mos.x < 0:
            mos.x += 10
        elif mos.x > 9:
            mos.x -= 10
        else:
            pass

        # 如果走完之后超过纵坐标最上边，那么减10回到同行的另一侧，类似贪吃蛇
        # 如果走完之后超过纵坐标最下边，那么加10回到同行的另一侧，类似贪吃蛇
        if mos.y < 0:
            mos.y += 10
        elif mos.y > 9:
            mos.y -= 10
        else:
            pass

        if tom.x == mos.x and tom.y == mos.y:
            tom.power += 10
            if tom.power > 100:
                tom.power = 100
            mouses.remove(mos)
            print('吃到了一条老鼠', mos.name)
        else:
            print('%s猫当前的体力值为%d：当前还剩老鼠%d条' % (tom.name, tom.power, len(mouses)))


