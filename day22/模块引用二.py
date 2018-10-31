# @Time :2018/8/21 002115:58
# @Author :Alex
# @File  :模块引用二.py
"""
使用from 模块 import 类、变量
"""
from Game import Dog, per
import random


class ModelImport:
    pass


# 通过导入的模块Dog创建一只狗
dog = Dog()
dog.attack = 600
dog.bite(per)
print('被%s咬过之后，%s还剩下%d血量' % (dog.name, per.name, per.hp))


for x in range(10):
    print(random.randint(-2, 2))
    random.choice

