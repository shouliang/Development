import re
import xlrd
import xlwt
import csv

workbook = xlrd.open_workbook(filename='r.xlsx')
sheet1 = workbook.sheet_by_index(0)

# 生成新的表格
workbook_new = xlwt.Workbook()
sheet1_new = workbook_new.add_sheet('newsheet1')
firstRow = []

# 提取生成表格
with open('newR.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    # 读取sheet1中的所有行
    for i in range(0, sheet1.nrows):
        r_content = sheet1.cell(i, 1).value                               # 获取要处理的单元格内容
        pattern = re.compile(r';  ([A-Z]{2,}\d{3,12}-[A-Z]{1}\d{0,})  ')  # 正则匹配并提取出想要的所有内容
        result1 = pattern.findall(r_content)
        pattern = re.compile(r' -- ([A-Z]{2,}\d{3,12}-[A-Z]{1}\d{0,})')
        result2 = pattern.findall(r_content)
        result = list(set(result1 + result2))                           # 将提取的内容后去重并转换成list格式

        firstRow = list(set(firstRow + result))
        firstRow = [val for val in firstRow if len(val) > 0]
        
        r_content_0 = sheet1.cell(i, 0).value                         # 获取要处理的单元格内容
        pattern = re.compile(r'(^[A-Z]{2,}\d{3,12}-[A-Z]{1}\d{0,})')  # 正则匹配并提取出想要的所有内容
        result0 = pattern.findall(r_content_0)
  
        result = result0 + result
        writer.writerow(result)


# 将提取的所有列写入第一行： 先读取再重新写入
allrows = []
with open('newR.csv', 'r') as csvfile:    
    csvreader = csv.reader(csvfile) 
    for row in csvreader: 
        newrow=row[0:1]
        for i in range(len(firstRow)):
            if firstRow[i] in row:
                newrow.append(1)
            else:
                newrow.append(0)
        allrows.append(newrow)       
        
firstRow.insert(0,'')

with open('newR.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(firstRow)
    for line in allrows:
        writer.writerow(line)

print(len(firstRow))