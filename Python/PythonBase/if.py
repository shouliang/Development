number = 23
guess = int(input('Enter an integer : '))

# if语句结尾处包含一个冒号，借此向Python指定接下来会有一块语句在后头
# 另外需注意elif关键字
# Python中不存在switch语句，可以通过if..elif..else语句来实现同样的事情

if guess == number:
    print('Congratulations, you guessed it.')
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')

print('Done')