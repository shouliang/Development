#!/bin/bash
# 字符串
your_name="runoob"

greeting="hello, "$your_name" !"
greeting_1="hello,${your_name} !"
echo $greeting $greeting_1

greeting_2='hello,'$your_name''
greeting_3='hello,${your_name}'
echo $greeting_2 $greeting_3

# 通过在变量名前加#，可以获得字符串的长度
string="abcd"
echo ${#string}

# 提取子字符串
string="runoob is a great site"
echo ${string:1:4}

# 通过在表达式中使用index的形式来查找子字符串
string="runoob is a great site"
echo `expr index "$string" io`
