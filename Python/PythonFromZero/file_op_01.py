# 将小说的主要人物记录在文件中

file4 = open('name_1.txt')
print(file4.readline())
file4.close()

# 逐行读取
file5 = open('name_1.txt')
for line in file5.readlines():
    print(line)
    print('=============')
file5.close()

file6 = open('name_1.txt')
# tell告诉文件当前指针位置
print('当前文件指针位置 %s:' % file6.tell())
file6.read(1)
print('当前文件指针位置 %s:' % file6.tell())

# seek表示相对偏移
file6.seek(0)
# seek若为两个参数的形式，第一个参数代表偏移位置
# 第二个参数：0:表示从文件开头位置偏移，1:表示从当前位置偏移，2:从文件结尾偏移ß
file6.seek(5, 0)
print('当前文件指针位置 %s:' % file6.tell())
file6.close()
