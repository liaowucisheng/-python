import random

answer = random.randint(1, 100)  # 产生随机数
counter = 0  # 计算猜了几次
while True:
    counter += 1
    number = int(input('请输入你猜的数字：'))
    if number < answer:
        print('再大一点')
    elif number > answer:
        print('再小一点')
    else:
        print("恭喜你猜对了！！！")
        break
print("你一共猜%d次才猜对了%d" % (counter, answer))
if counter > 7:
    print('你的智商余额不足吧！？')