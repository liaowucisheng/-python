# -*- coding:utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/23 23:26
# File: 写一个程序判断输入的正整数是不是回文素数

from 实现判断一个数是不是回文数的函数 import judge_palindrome
from 实现判断一个数是不是素数的函数 import is_prime

if __name__ == '__main__':
    num = int(input("请输入一个数以判断其是否回文兼素数："))
    print(is_prime(num) and judge_palindrome(num))
