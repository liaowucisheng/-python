"""
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
"""
# 思路： 设置生成2到12的随机数，分第一回合和其它回合
# 在python中的random.randint(a,b)用于百生成一个指定范围内的整数。其中参数度a是下限，参数b是上限，生成的问随答机数n: a <= n <= b。
from random import randint

while True:
    num_1 = randint(1, 6) + randint(1, 6)
    print('你摇出来的骰子是：', num_1)
    if num_1 == 7 or num_1 == 11:
        print('玩家赢！！！')
        break
    elif num_1 == 2 or num_1 == 3 or num_1 == 12:
        print('庄家赢了^_^')
        break
    else:
        while True:
            num_2 = randint(1, 6) + randint(1, 6)
            print('你摇出来的骰子是：', num_2)
            if num_2 == num_1:
                print('玩家赢了！！！')
                exit()
            elif num_2 == 7:
                print('庄家赢了^_^')
                exit()
