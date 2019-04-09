# 将小说的主要人物记录在文件中

# 写入,w = write,默认为read
file1 = open('name.txt', 'w')
file1.write('诸葛亮')
file1.close()

# 读取,默认就是为读取
file2 = open('name.txt')
print(file2.read())
file2.close()

# 附加 a = append
file3 = open('name.txt', 'a')
file3.write('刘备')
file3.close()


