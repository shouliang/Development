# break终止循环语句的执行
while True:
    s = input('Enter something :')
    if s == 'quit':
        break
    print('Length of the string is',len(s))

print('Done')