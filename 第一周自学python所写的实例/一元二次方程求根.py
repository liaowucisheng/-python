#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/24 16:16
# File: 一元二次方程求根
import math


def quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return '方程无解'
    x1 = (- b + math.sqrt(d)) / (2 * a)
    x2 = (- b - math.sqrt(d)) / (2 * a)
    return x1, x2


if __name__ == '__main__':
    a, b, c = map(float, input('请按顺序输入方程的a,b,c值，记得以空格隔开：').split())
    print("方程的解为：", quadratic(a, b, c))
