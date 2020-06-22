#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/6/16 17:01
# File: 自动轨迹绘制
import turtle as t

t.Turtle().screen.delay(0)    # 画笔延迟设置为0
t.title('自动绘制')
t.setup(800, 600, 0, 0)  # 前两个长宽，后两个初始位置x,y
t.pencolor('red')
t.pensize(4)

# 数据读取，文件内，每行第一个为距离，第二个为判断向左向右转，第三四五个为画笔颜色
datals = []
f = open('自动绘制相关数据.txt')
for line in f:
    line = line.replace('\n', '')
    datals.append(list(map(eval, line.split(','))))
f.close()
# 绘图
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.rt(datals[i][2])
    else:
        t.lt(datals[i][2])

t.done()
