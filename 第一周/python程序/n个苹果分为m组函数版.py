# -*- coding:utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/23 20:12
# File: n个苹果分为m组函数版

def factorial(num):
    return_num = 1
    for i in range(1, num + 1):
        return_num *= i
    return return_num

n = int(input('请输入苹果总数：'))
m = int(input('请输入要分成的组数：'))
print('%d 个苹果分成 %d 组总共有 %d 种分法。' % (n, m, factorial(n) / factorial(m) / factorial(n - m)))