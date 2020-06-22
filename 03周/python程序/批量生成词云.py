#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/6/20 12:40
# File: 批量生成词云
import os
import jieba
import wordcloud


def many_word_cloud(open_location):
    file_list = []
    for i in os.listdir(open_location):
        file_list.append(os.path.join(open_location, i))
    for j in range(len(file_list)):
        with open(file_list[j], 'r', encoding='utf-8') as f:
            ls = jieba.lcut(f.read())
            txt = " ".join(ls)
            w = wordcloud.WordCloud(font_path="msyh.ttc", width=1920, height=1080, background_color='white', max_words=30)
            w.generate(txt)
            w.to_file(file_list[j][:-4] + '.png')


if __name__ == '__main__':
    file_name = input("请输入文件路径：")
    many_word_cloud(file_name)
