#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 了无此生
# DateTime: 2020/5/26 21:32
# File: 定义一个类描述数字时钟

from time import sleep

class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    # 走字
    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.second == 60:
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    # 显示时间
    def show(self):
        return '%02d:%02d:%02d' % (self.hour, self.minute, self.second)

# 定义主函数
def main():
    clock = Clock(21, 53, 00)
    while True:
        print(clock.show())
        clock.run()
        sleep(1)


if __name__ == '__main__':
    main()
