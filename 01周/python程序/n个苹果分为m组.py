# 将8个苹果分成四组每组至少一个苹果有多少种方案，组合数 Cnm(n为上标，m为下标) = n!/(m!*(n-m)!)
n = int(input('请输入苹果总数：'))
m = int(input('请输入要分成的组数：'))
n_factorial = 1
for i in range(1, n + 1):
    n_factorial *= i
m_factorial = 1
for i in range(1, m + 1):
    m_factorial *= i
n_m_factorial = 1
for i in range(1, n - m + 1):
    n_m_factorial *= i
print('%d 个苹果分成 %d 组总共有 %d 种分法。' % (n, m, n_factorial / m_factorial / n_m_factorial))