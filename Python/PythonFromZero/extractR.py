# coding=utf-8
import re
import xlrd
import csv

file = 'r.xlsx'
wb = xlrd.open_workbook(filename=file)  # 打开文件
sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格

with open('newR.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['newR'])
    for i in range(1, sheet1.nrows):
        r_content = sheet1.cell(i, 17).value
        pattern = re.compile(r';  ([A-Z]{2,}\d{10}-[A-Z]{1}\d{0,})  ')
        result1 = pattern.findall(r_content)

        pattern = re.compile(r' -- ([A-Z]{2,}\d{7,}-[A-Z]{1}\d{0,})')
        result2 = pattern.findall(r_content)

        result = list(set(result1 + result2))
        writer.writerow(result)
