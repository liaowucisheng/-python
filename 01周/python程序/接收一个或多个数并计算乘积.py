#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/25 0:29
# File: 接收一个或多个数并计算乘积

def product(x, *y):
    s = 1
    for n in y:
        s = s * n
    print(x * s)

if __name__ == '__main__':
    product(1)
    product(1, 2)
    product(1, 2, 3)
    product(1, 2, 3, 4)
    product(1, 2, 3, 4, 5)
    product(1, 2, 3, 4, 5, 6)
    product(1, 2, 3, 4, 5, 6, 7)