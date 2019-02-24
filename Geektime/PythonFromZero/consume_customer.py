# import queue
#
# q = queue.Queue()
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.get())
# print(q.get())
# print(q.get())

# 生产者消费者

from threading import Thread, current_thread
import time
import random
from queue import Queue

queue = Queue(5)


class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生成了数据 %s' % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s秒' % (name, t))


class ConsumerThread(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print('消费者 %s 消耗了数据 %s' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s 秒' % (name, t))


# 生产者少消费者多的情况
# p1 = ProducerThread(name='p1')
# p1.start()
# c1 = ConsumerThread(name='c1')
# c1.start()
# c2 = ConsumerThread(name='c2')
# c2.start()

# 生产者多消费者少的情况
p1 = ProducerThread(name='p1')
p1.start()
p2 = ProducerThread(name='p2')
p2.start()
p3 = ProducerThread(name='p3')
p3.start()
c1 = ConsumerThread(name='c1')
c1.start()
