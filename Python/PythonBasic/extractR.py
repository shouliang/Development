import re
import xlrd
import xlwt

workbook = xlrd.open_workbook(filename='r.xlsx')
sheet1 = workbook.sheet_by_index(0)

# 生成新的表格
workbook_new = xlwt.Workbook()
sheet1_new = workbook_new.add_sheet('newsheet1')

# 读取sheet1中的所有行
for i in range(0, sheet1.nrows):
    r_content = sheet1.cell(i, 1).value                             # 获取要处理的单元格内容
    pattern = re.compile(r';  ([A-Z]{2,}\d{10}-[A-Z]{1}\d{0,})  ')  # 正则匹配并提取出想要的所有内容
    result1 = pattern.findall(r_content)
    pattern = re.compile(r' -- ([A-Z]{2,}\d{7,}-[A-Z]{1}\d{0,})')
    result2 = pattern.findall(r_content)
    result = list(set(result1 + result2))                           # 将提取的内容后去重并转换成list格式

    row_content = sheet1.row_values(i)                              # 获取当前行
    result = row_content[0:1] + result                              # 从当前行中去掉已处理的单元格，并和处理后的结果合并

    # 写入新的表格: 以逐行逐利的方式
    for j in range(len(result)):
        sheet1_new.write(i, j, result[j])
    
    print("dealing row at index "+ str(i))
 
    # 保存新的表格
    workbook_new.save('newr.xls')