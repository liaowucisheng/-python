#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/24 20:49
# File: 定义函数的五种参数

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、关键字参数、命名关键字参数

# 默认为平方，可以任意次幂
def power(x, n=2):
    s = 1
    while n:
        s *= x
        n -= 1
    return s


# 学生注册的函数
def enroll(name, gender, age=20, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def add_end1(L=[]):
    L.append('END')
    return L


# 在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数（如下面的’*d‘）允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 关键字参数Z（如下面的’**e‘）允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def f1(a, b=0, *d, **e):
    print('a=', a, 'b=', b, 'd=', d, 'e=', e)
nums1 = [1, 2, 3]
f1(3, 2, *nums1, age=12, city='beijing')
# a= 3 b= 2 d= (1, 2, 3) e= {'age': 12, 'city': 'beijing'}

# 命名关键字参数：*后面的参数被视为命名关键字参数。
def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
f2(1, 2, d='beijing', city='nanjin', gender='大一' )
# a= 1 b= 2 c= 0 d= beijing kw= {'city': 'nanjin', 'gender': '大一'}

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('lwcs', 27, ['男', '实际上20周岁', '身家清白'], city='beijing', job=['student', '单身狗'])
# 若删去’city='beijing', ‘， 则报错：person() missing 1 required keyword-only argument: 'city'

if __name__ == '__main__':
    f1(1, 2)
    f1(1, 2, 'i', 'j')    # a= 1 b= 2 d= ('i', 'j') e= {}
    f1(1, 2, 'i', 'i', x=99)    # a= 1 b= 2 d= ('i', 'i') e= {'x': 99}

    args = (1, 2, 3)
    kw = {'asd': 100, 'cj': 'fewfd'}
    f1(*args, **kw)    # a= 1 b= 2 d= (3,) e= {'asd': 100, 'cj': 'fewfd'}

    print(power(5))
    enroll('郑峻杰', '大二')
    enroll('lwcs', '大一', city='shanghai', age=18)
    enroll('dsc', '高三', 18, 'guangzhou')
    # 默认参数很有用，但使用不当，也会掉坑里。
    print(add_end1())  # ['END']
    print(add_end1())  # ['END', 'END']
    print(add_end1())  # ['END', 'END', 'END']
    print(add_end2())  # ['END']
    print(add_end2())  # ['END']
    print(add_end2())  # ['END']
