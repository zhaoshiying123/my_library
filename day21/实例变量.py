# @Time :2018/8/21 002111:32
# @Author :Alex
# @File  :实例变量.py


class Fo:
    # 类变量
    count = 1


# 定义两个实例
f1 = Fo()
f2 = Fo()

"""
这里的 f1.count = 2 就类似于使用 self.count = 2， self表示本身的实例对象
self的形式对类变量赋值，真实的类变量不改，该对象的这个变量变成实例变量
"""
f2.count = 2

print(f1.count, f2.count, Fo.count)
