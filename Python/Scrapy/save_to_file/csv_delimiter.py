import csv

with open('data2.csv', 'w') as csvfile:
    # 默认已,逗号分隔，通过delimiter参数可以指定分隔符
    writer = csv.writer(csvfile, delimiter=' ')
    # wrirerow 每次写入一行
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', '20'])
    writer.writerow(['10002', 'Bob', '22'])
    writer.writerow(['1003', 'Jordan', '21'])
