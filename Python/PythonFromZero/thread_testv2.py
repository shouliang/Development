import threading
from threading import current_thread


class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run')
        print(current_thread().getName(), 'stop')


t1 = MyThread()
t1.start()
t1.join()  # 线程同步，执行完后最后在执行主线程的结束

print(current_thread().getName(), 'main process end')
