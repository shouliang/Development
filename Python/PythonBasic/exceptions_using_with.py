# coding=utf-8

# with自动释放资源
with open("poem.txt") as f:
    for line in f:
        print(line, end='')