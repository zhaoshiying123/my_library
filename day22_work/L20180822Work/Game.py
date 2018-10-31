# @Time :2018/8/22 002210:19
# @Author :Alex
# @File  :Game.py

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
    tom.move()

    # 10只老鼠开始移动
    for mos in mouses:
        mos.move()
        if tom.x == mos.x and tom.y == mos.y:
            tom.eatMouse()
            mouses.remove(mos)
            print('吃到了一条老鼠', mos.name)
        else:
            print('%s猫当前的体力值为%d：当前还剩老鼠%d条' % (tom.name, tom.power, len(mouses)))


