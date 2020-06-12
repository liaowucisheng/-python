#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/6/1 14:20
# File: 面向对象-编程熟悉1

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter 方法
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    # 修改器 - setter 方法
    @name.setter
    def name(self, name):
        self._name = name
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 12:
            print('%s正在看猫和老鼠' % self._name)
        else:
            print('%s正在吃鸡' % self._name)


def main():
    resident1 = Person('隔壁老王', 30)
    print(resident1.name, resident1.age)
    resident1.name = '小头爸爸'
    resident1.age = 35
    resident2 = Person('大头儿子', 10)
    resident1.play()
    resident2.play()
    print(Person.name)

if __name__ == '__main__':
    main()
