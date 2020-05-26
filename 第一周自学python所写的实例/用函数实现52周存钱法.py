# -*- coding:utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/24 0:13
# File: 用函数实现52周存钱法

"""
52周存钱法，即52周阶梯式存钱法，是国际上非常流行的存钱方法。
按照52周存钱法，存钱的人必须在一年52周内，每周递存10元
例子：
第1周：10元，第2周：20元，第3周：30元·······一直到第52周：520元。
总计：10+20+30+······+520 = 13780元
"""


def save_money(num):
    sum = 0
    for n in range(1, 53):
        sum += num
        print('现在是第%d周，你要存入的金额是%d元，累计存入金额为：%d元' % (n, num, sum))
        num += 10
    return sum


if __name__ == '__main__':
    first_money = int(input('请输入你第一周要存的初始金额：'))
    print("一年后你将存下的钱为：%d元" % save_money(first_money))
