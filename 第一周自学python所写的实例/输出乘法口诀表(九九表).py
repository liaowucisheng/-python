for i in range(1, 10):
    for j in range(1, 10):
        print('%d*%d=%d' % (j, i, i * j), end='\t')
        if i == j:
            break
    print()
