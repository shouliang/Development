# continue跳过当前循环块中的剩余语句，并继续该循环的下一次迭代
while True:
    s = input('Enter something :')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
