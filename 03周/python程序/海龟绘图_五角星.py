#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/6/16 14:12
# File: 海龟绘图
from turtle import *
# 五角星
color('yellow', 'red')
pensize(10)
begin_fill()
while True:
    forward(300)
    rt(144)    # 与right(144)作用相同，都是向右转144度
    if abs(pos()) < 1:
        break
end_fill()
done()