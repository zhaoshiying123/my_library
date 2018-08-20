# @Time :2018/8/20 002015:09
# @Author :Alex
# @File  :Tiger.py

"""
创建一个老虎类
"""


class Tiger:
    # 定义老虎的属性特征
    height = 100
    weight = 150
    age = 10

    '''
    定义老虎的行为特征
    '''
    def t_sleep(self):
        print('老虎在睡觉')


# 创建一只老虎
tiger = Tiger()
print('这只的重量是：', tiger.weight)
print('这只老虎的年龄是：', tiger.age)
tiger.t_sleep()
