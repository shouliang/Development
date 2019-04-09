#!/bin/bash

# if 与 fi 相互匹配
if condition
then
    "command1"
else
    "command"
fi

# for in
# in列表可以包含字符串、文件名
# in列表是可选的，如果不用它，默认使用命令行的位置参数
for loop in 1 2 3 4 5
do
	echo "The value is: $loop"
done

for str in 'This is a string'
do
	echo $str
done

int=1
while (( $int <=5))
do
	echo $int
	let "int++"
done

# echo "按下<CTRL-D>退出"
# echo -n "输入你喜欢的网站名"
# while read FILM
# do
# 	echo "是的，$FILM 是一个好网站"
# done	



a=0

until [ ! $a -lt 10 ] 
do
	echo $a
	a=`expr $a + 1`
done



# echo "输入 1 到 4 之间的数字："
# echo "你输入的数字为："
# read aNum
# case $aNum in
# 	1) echo "你选择了 1"
# 	;;
# 	2) echo "你选择了 2"
# 	;;
# 	3) echo "你选择了 3"
# 	;;
# 	4) echo "你选择了 4"
# 	;;
# 	*) echo "你没有输入 1 到 4 之间的数字"
# 	;;
# esac

# case 值 in
# 模式1)
# 注意只有一个右括号
# case 与 esac(就是case反过来拼写) 相互匹配
while :
do
	echo -n "输入 1 到 5 之间的数字:"
	read aNum
	case $aNum in
		1|2|3|4|5) echo "你输入的数字为 $aNum"
		;;
		*) echo "你输入的数字不是1 到 5 之间的！ 游戏结束"
			break
		;;
	esac
done			






