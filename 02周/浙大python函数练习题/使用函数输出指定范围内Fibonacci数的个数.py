#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/27 20:29
# File: 使用函数输出指定范围内Fibonacci数的个数
"""
这个程序就是典型的不断试错，开始时fib()函数的else忘记return，
后来，按我的思路来，运行到fib(6) = 8就出错，仔细检查，
发现i的值是if i ==1 or i == 2，而在调用它的PrintFN()函数内，
range()是从0开始生成的，今天的代码写得我怀疑人生，各种报错
"""
def fib(i):
    if i == 0 or i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)

def PrintFN(m, n):
    a = []
    for b in range(25):
        if m <= fib(b) <= n:
            a.append(fib(b))
    return a

m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
b=fib(i)
print("fib({0}) = {1}".format(i,b))
fiblist=PrintFN(m,n)
print(len(fiblist))