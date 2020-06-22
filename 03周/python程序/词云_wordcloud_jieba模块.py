#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/6/17 17:28
# File: 词云_wordcloud_jieba模块
"""
wordcloud模块目前没有python3.8的版本，这程序是在python3.7.7的环境下运行的
"""
import jieba
import wordcloud
txt = "俄格而人格侮辱而特认为二锅头如果还人iu合噶尔热高热高热hi古我iu复合物i啊防护额外IP-我i为OK福克斯的i维尔哦i额外和肥瑞格i而回uurge瑞给3iOKi热i而回顾热红外而饿哦i然后给i热舞和i二级哦呜 哦ii而平湖热火偶然配合为人平和俄容二虎微盘偶尔会人"
w = wordcloud.WordCloud(width = 1000, font_path = "F:\BaiduNetdiskDownload\品牌字体\腾讯字体\TTTGB-Medium.ttf", height = 700, background_color='red', colormap='Blues')
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("词云_wordcloud_jieba2.png")