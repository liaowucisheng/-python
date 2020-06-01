#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/27 19:59
# File: 使用函数统计指定数字的个数

"""
本题要求实现一个统计整数中指定数字的个数的简单函数。
CountDigit(number,digit )
其中number是整数，digit为[1, 9]区间内的整数。函数CountDigit应返回number中digit出现的次数。
"""


def CountDigit(number, digit):
    a = 0
    if number < 0:
        t = -number
    else:
        t = number
    while t > 0:
        s = t % 10
        if s == digit:
            a += 1
        t //= 10
    return a


if __name__ == '__main__':
    number, digit = input().split(' ')
    number = int(number)
    digit = int(digit)
    count = CountDigit(number, digit)
    print("Number of digit %d in " % digit + str(number) + ":", count)
