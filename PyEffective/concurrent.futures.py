# coding=utf-8
import time


# 基三两数的最大公约数
def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [(1963309, 2265973), (2030677, 3814172),
           (1551645, 2229620), (2039045, 2020802)]

start = time.time()
results = list(map(gcd, numbers))
print(results)
end = time.time()

print('Took %.3f seconds' % (end - start))
