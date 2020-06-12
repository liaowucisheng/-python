#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/28 1:41
# File: 缩写词

"""
缩写词是由一个短语中每个单词的第一个字母组成，均为大写。例如，CPU是短语“central processing unit”的缩写。
函数接口定义：
acronym(phrase);
phrase是短语参数，返回短语的缩写词
"""


def acronym(phrase):
    s = ""
    p = phrase.title()  # Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
    a = p.split()  # Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
    for i in range(0, len(a)):
        s += a[i][0]
    return s


phrase = input()
print(acronym(phrase))

