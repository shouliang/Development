import csv 

csvfile = open('testc.csv', 'w') 
writer = csv.writer(csvfile)
writer.writerow(["zhangsan",100]) 
writer.writerow(["lisi",80]) 
writer.writerow(["wangwu",90]) 
csvfile.close()