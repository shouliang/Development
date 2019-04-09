#!/bin/bash

# 输出重定向
echo "test redirct" >> redirect.txt

who > users

# >> 已追加的方式重定向到file
who >> users

# 输入重定向 wc: word count, l 统计行数
wc -l < users


# 标志输入、输出、错误文件的文件描述法分别为：0、1、2

# 如果希望执行某个命令，但又不希望在屏幕上显示输出结果
# 那么可以将输出重定向到 /dev/null