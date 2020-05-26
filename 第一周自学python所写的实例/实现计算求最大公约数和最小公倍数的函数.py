# -*- coding:utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/23 20:47
# File: 实现计算求最大公约数和最小公倍数的函数

# 求最大公约数的函数
def max_common_divisor(num1, num2):
    if num1 > num2:
        (num1, num2) = (num2, num1)
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


# 求最小公倍数的函数
def min_common_multiple(num1, num2):
    return num1 * num2 // max_common_divisor(num1, num2)


# 主函数部分
if __name__ == '__main__':
    a = int(input('请输入第一个数：'))
    b = int(input('请输入第二个数：'))
    print('最大公约数是：%d，最小公倍数是：%d' % (max_common_divisor(a, b), min_common_multiple(a, b)))
