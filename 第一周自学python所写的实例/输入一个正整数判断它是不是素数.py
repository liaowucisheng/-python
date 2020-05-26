# sqrt() 方法返回数字x的平方根。再计算质数时，仅需计算到它的平方根即可
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是质数' % num)
else:
    print('%d不是质数，可被%d整除' %(num, x))