import time

# time.time()1970年1月1日到现在的描述
print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d'))
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y/%m/%d'))

print('---------')
import datetime

print(datetime.datetime.now())
add_ten_minutes = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + add_ten_minutes)

# 指定日期后的多少天
one_day = datetime.datetime(2018, 10, 1)
add_ten_days = datetime.timedelta(days=10)
print(one_day + add_ten_days)
