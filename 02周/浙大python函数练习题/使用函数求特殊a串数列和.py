#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/27 18:39
# File: 使用函数求特殊a串数列和
def fn(a, b):
    sum = res = 0
    for i in range(b):
        sum += a    #sum是a第i+1位数的值
        a = a * 10
        res += sum
    return res

a, b = input().split()
s = fn(int(a),int(b))
print(s)