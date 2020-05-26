# -*- coding:utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/23 23:20
# File: 实现判断一个数是不是素数的函数

# 判断一个数是否素数
def is_prime(num):
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True if num != 1 else False

if __name__ == '__main__':
    num = int(input('请输入一个数以判断其是否素数：'))
    print(is_prime(num))