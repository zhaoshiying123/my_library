# @Time :2018/8/21 002115:06
# @Author :Alex
# @File  :模块引用.py

"""
如果想要导入的模块包含包名，包名不可以是数字开头
"""
import 实例变量 as Sl


class Ok:
    success = 1


# sl 是一个模块，他可以找到模块下面静态变量，但是不能直接调用类里面的静态变量
s = Sl.Fo()

print(Sl.Fo.count)
print(s.name)
print(s.count)
