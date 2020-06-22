#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/6/14 20:44
# File: 文件操作
import os
print(os.name) # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统

with open('E:\\study_python\\02周\\学生信息.txt', 'r', encoding='utf-8') as f:
    print(f)
    # for line in f.readlines():
    #     print(line, end='')
    # print(f.readline())
    # for line in f.readline():
    #     print(line, end='|\n')
    # for line in f.readlines():
    #     print(line.strip(), end='|\n')
    # # print(f.read(55))
# with open('E:\\study_python\\02周\\第二周自学python心得.md', 'rb') as ejz:
#     print(ejz)

with open('E:\\study_python\\02周\\学生信息.txt', 'w') as f:
    f.writelines('阿五\t2018119104\t169\t670')

with open('E:\\study_python\\02周\\学生信息.txt', 'r') as f:
    print(f.readlines())
# 廖雪峰我日你大爷，老子的文件数据就这样没了