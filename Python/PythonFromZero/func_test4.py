# 装饰器
import time


# print(time.time())


# def i_can_sleep():
#     time.sleep(3)
#
#
# start_time = time.time()
# i_can_sleep()
# stop_time = time.time()
# print('函数运行了 %s 秒' % (stop_time - start_time))


# 演变成装饰器的写法
def mytimer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('函数运行了 %s 秒' % (stop_time - start_time))

    return wrapper


@mytimer
def i_can_sleep():
    time.sleep(3)


i_can_sleep()
