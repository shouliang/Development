number = 23
running = True

# while语句可以拥有else子句作为可选选项
while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, your guessed it.')
        running = False
    elif guess < number:
        print('No, it is a litter higher than that.')
    else:
        print('No, it is a litter lower than that.')
else:
    print('The while loop is over.')

print('Done')

