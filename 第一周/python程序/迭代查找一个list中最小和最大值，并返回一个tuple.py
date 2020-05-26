#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/25 1:22
# File: 迭代查找一个list中最小和最大值，并返回一个tuple

def fin_min_and_max(L):
    if len(L) == 0:
        print('list为空')
        return (None, None)
    else:
        min, max = L[0], L[0]
        for i in L:
            if min > i:
                min = i
            if max < i:
                max = i
        return (min, max)


# 测试
if fin_min_and_max([]) != (None, None):
    print('测试失败!')
elif fin_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif fin_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif fin_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
