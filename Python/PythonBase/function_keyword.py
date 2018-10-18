# 关键字参数
# 好处1：可以不用考虑参数的顺序
# 好处2：可以只对希望赋值的参数赋值
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)
