# 在函数中接收元组
def powersum(power, *args):
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powersum(2, 10))
print(powersum(2, 3, 4))
print(powersum(3,10))
