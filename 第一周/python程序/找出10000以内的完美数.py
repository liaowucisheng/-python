"""
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解
"""
for i in range(1, 10000):
    sum_num = 0
    # 生成1到i/2的数，由于'float' object cannot be interpreted as an integer，故用‘//’，由于range(a, b)是生成包含a到不包含b的数，所以要‘+1’
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            sum_num += j
            # 找到了完美数，接下来就是输出它啦
            if sum_num == i and j == i // 2:
                print(i, end='')
                for k in range(1, i // 2 + 1):
                    if i % k == 0 and k != 1:
                        print('+', end='')
                        print(k, end='')
                    elif k == 1:
                        print('=%d' % k, end='')
                print()
