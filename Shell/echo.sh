#!/bin/bash
# 显示普通字符串
echo "It is a test"

# 显示转义字符
echo "\"It is a test\""

# 显示变量
read name
echo "$name It is a test"

# 显示换行 -e 开启转义 \n 换行
echo -e "OK! \n"
echo "It is a test for \n"

# 显示不换行 -e 开始转义 \c 不换行
echo -e "OK! \c"
echo "It is a test for \c"

# 显示结果定向到文件
echo "It is a test into file" > myfile

# 原样输出
echo '"$name\"'

# 显示命令执行结果
echo `date`