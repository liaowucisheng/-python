#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/27 17:02
# File: 计算出文件里学生最高GPA并打印

"""
源：<https://www.icourse163.org/course/ZJU-1206456840> 8.3使用对象编写程序
"""

class StudentGPA(object):
    def __init__(self, name, num, credits, qpoints):
        """

        :param name: 姓名
        :param num: 学号
        :param zxf: 总学分
        :param zjd: 总绩点
        """
        self.name = name
        self.num = num
        self.credits = credits
        self.qpoints = qpoints
    # 以下三个方法可省略
    def get_name(self):
        return self.name

    def get_credits(self):
        return self.credits

    def get_qpoints(self):
        return self.qpoints
    # 返回总学分除以总绩点的值，即GPA的值
    def calculate_GPA(self):
        return self.qpoints / self.credits

# 定义make_student方法，用于创建对象
def make_student(infoStr):
    # infoStr为文件中的一行内容，创建一个学生对象，返回StudentGPA对象
    name, num, credits, qpoints = infoStr.split("\t")  # Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
    return StudentGPA(name, num, int(credits), int(qpoints))


def main():
    filename = input("请输入要打开的文件名：")
    infile = open(filename, mode='r', encoding='utf8')    # 只读，编码方式为UTF-8
    best = make_student(infile.readline())
    # best对象存放GPA最高的学生
    for line in infile:
        s = make_student(line)
        if s.calculate_GPA() > best.calculate_GPA():
            best = s
    infile.close()  # close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作
    print(best.name, best.num, best.credits, best.qpoints, best.calculate_GPA())


if __name__ == '__main__':
    main()
