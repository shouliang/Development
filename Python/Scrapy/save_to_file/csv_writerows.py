import csv

with open('data3.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    # wrirerows 写入多行
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['10001', 'Mike', '20'], ['10002', 'Bob', '22'], ['1003', 'Jordan', '21']])
