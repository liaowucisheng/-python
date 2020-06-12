#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/6/1 16:29
# File: 面向对象-编程熟悉2

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def paly(self):
        if self._age >= 18:
            print('%d岁的%s不想谈恋爱了' % (self._age, self._name))
        else:
            print("%d岁的%s没时间谈恋爱" % (self._age, self._name))


class Students(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%d岁在读%s的%s正在学习%s' % (self._age, self._grade, self._name, course))


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print("%s级%d岁的%s老师正在教导%s" % (self._title, self._age, self._name, course))


def main():
    person1 = Person('蔡徐坤', 24)
    person2 = Person('肖战', 25)
    student1 = Students('xxs', 6, '一年级')
    person1.paly()
    person1.name = person2.name
    person1.paly()
    student1.study('Python')
    student1.paly()
    teacher1 = Teacher('老苗', 50, '大二')
    teacher1.teach('数据结构')


if __name__ == "__main__":
    main()
