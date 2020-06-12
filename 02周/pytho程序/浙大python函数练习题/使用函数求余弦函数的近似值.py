#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/27 23:41
# File: 使用函数求余弦函数的近似值

"""
第6章函数-5 使用函数求余弦函数的近似值 (20分)
本题要求实现一个函数，用下列公式求cos(x)近似值，精确到最后一项的绝对值小于eps（绝对值小于eps的项不要加）：
cos (x) = x^0 / 0! - x^2 / 2! + x^4 / 4! - x^6 / 6! + ?
函数接口定义：funcos(eps,x ),其中用户传入的参数为eps和x；函数funcos应返回用给定公式计算出来，保留小数4位。
"""
def jiechen(n):
    if n == 0:
        return 1
    else:
        return n * jiechen(n - 1)

def funcos(eps, x):
    s = 0
    i = 0
    j = 1
    while x ** i / jiechen(i) >= eps:
        s += j * x ** i / jiechen(i)
        i += 2
        j = -j
    return s


eps=float(input())
x=float(input())
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))