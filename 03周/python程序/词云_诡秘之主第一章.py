#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/6/18 0:43
# File: 词云_诡秘之主第一章
import jieba
import wordcloud
f = open("诡秘之主_第一章_绯红.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width = 1920, height = 1080, background_color='white')
w.generate(txt)
w.to_file("词云_诡秘之主_第一章_绯红.png")