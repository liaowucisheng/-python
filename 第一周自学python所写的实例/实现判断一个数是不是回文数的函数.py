# -*- coding:utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/23 23:05
# File: 实现判断一个数是不是回文数的函数

def judge_palindrome(a):
    b = 0
    c = a
    while a:
        b = b * 10 + a % 10
        a //= 10
    return b == c

if __name__ == '__main__':
    num = int(input('请输入一个整数，以判断其是否回文：'))
    print(judge_palindrome(num))
