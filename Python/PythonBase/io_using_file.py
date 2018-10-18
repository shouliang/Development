poem = '''\
Programming is fun
when the work is done
if you wanna make your work also fun:
    use Python
'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

# 向文件中写入文本
# 默认为阅读('r'ead)模式
f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')

f.close()