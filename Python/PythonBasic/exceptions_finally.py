# coding=utf-8
import sys
import time

# finally总是被执行，一般执行释放资源的操作：如关闭文件，关闭数据库连接等
f = None
try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print('Press ctrl + c now')
        time.sleep(2)
except IOError:
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print('!! You cancelled the reading from the file')
finally:
    if f:
        f.close()
    print('Cleaning up: Closed the file')