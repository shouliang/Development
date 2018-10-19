#!/bin/bash

# 传递参数
echo "Shell 传递参数实例"
echo "执行的文件名: $0"
echo "执行的文件名: $1"
echo "执行的文件名: $2"
echo "执行的文件名: $3"

echo "参数个数为: $#"
echo "传递参数作为一个字符串显示: $*"

echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done

