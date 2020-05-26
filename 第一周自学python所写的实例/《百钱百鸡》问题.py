"""
百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
注释的代码来自：https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/05.%E6%9E%84%E9%80%A0%E7%A8%8B%E5%BA%8F%E9%80%BB%E8%BE%91.md
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
"""
# 15x + 9y + z = 300, x + y + z = 100
# x < 100 / 5 = 20, y < 100 / 3 = 33
for x in range(20):
    for y in range(33 - x):
        z = 100 - x - y
        if 15 * x + 9 * y + z == 300 and x + y + z == 100:
            print('公鸡有%d只，母鸡有%d只，小鸡有%d只' % (x, y, z))