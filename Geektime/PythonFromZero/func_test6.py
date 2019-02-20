# 自定义上下文管理器
f = open('name.txt')
try:
    for line in f:
        print(line)
finally:
    f.close()

# with就是上下文管理器，出错时会关闭文件
with open('name.txt') as f:
    for line in f:
        print(line)
