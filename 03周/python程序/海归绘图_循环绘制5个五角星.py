#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/6/16 15:13
# File: 海归绘图_循环绘制5个五角星
from turtle import *

def drawStar(x, y):
    pu()    # 移动时不绘画
    goto(x, y)    # 跳到坐标(x, y)，由于上面有一句pu()，故该过程不画出来
    pd()    # 移动时绘图，注释掉的话就只剩箭头在动
    # set heading: 0
    seth(0)    #初始角度
    for i in range(5):
        fd(40)    # forward(40)
        rt(144)    # right(144)

for x in range(0, 250, 50):
    color('red', 'yellow')
    print(x)
    drawStar(x, -100)

done()