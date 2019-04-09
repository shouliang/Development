#!/bin/bash
# 数组
# 定义数组：数组名=(值1 值2 ... 值n)
my_array=(A B "C" D)

# 读取数组${数组名[下标]}
echo "第一个元素为：${my_array[0]}"
echo "第二个元素为：${my_array[1]}"
echo "第三个元素为：${my_array[2]}"
echo "第四个元素为：${my_array[3]}"

# 获得数组中的所有元素
echo "数组元素为: ${my_array[*]}"
echo "数组元素为: ${my_array[@]}"

# 取得数组元素的个数
echo "数组元素的个数为: ${#my_array[*]}"
echo "数组元素的个数为: ${#my_array[@]}"
