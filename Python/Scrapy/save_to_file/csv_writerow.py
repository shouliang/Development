import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    # wrirerow 每次写入一行
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', '20'])
    writer.writerow(['10002', 'Bob', '22'])
    writer.writerow(['1003', 'Jordan', '21'])
