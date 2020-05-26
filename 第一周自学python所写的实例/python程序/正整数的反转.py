number = int(input('number = '))
reversed_number = 0
while number > 0:
    reversed_number = reversed_number * 10 + number % 10
    number = number // 10
print('反转后是：%d' % reversed_number)
