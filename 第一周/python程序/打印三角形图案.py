# *
# **
# ***
# ****
# *****
#     *
#    **
#   ***
#  ****
# *****
#     *
#    ***
#   *****
#  *******
# *********

row = int(input('请输入要打印的行数：'))
for i in range(row):
    # 以一个'*_'为单位，第几行输出几遍，结束换行用‘ print() ’
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
    for k in range(i * 2 + 1):
        print('*', end='')
    print('')