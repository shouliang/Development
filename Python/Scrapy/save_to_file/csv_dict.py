import csv

with open('data_dict.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 写入字典
    writer.writerow({'id': '10004', 'name': 'Durant', 'age': 22})
