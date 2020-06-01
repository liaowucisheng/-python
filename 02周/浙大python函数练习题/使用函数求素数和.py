#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/27 19:43
# File: 使用函数求素数和

def prime(a):
    for i in range(2, int(a ** 0.5) + 1, 1):
        if (a % i)== 0:
            return False
    return True if a != 1 else False

def PrimeSum(m, n):
    sum = 0
    for a in range(m, n):
         if prime(a):
             sum += a
    return sum

m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))