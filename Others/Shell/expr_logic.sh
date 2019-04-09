#!/bin/bash

# 逻辑运算符
# &&:逻辑AND ||:逻辑的OR
a=10
b=20

if [[ $a -lt 100 && $b -gt 100 ]]; 
then
	echo "返回true"
else
	echo "返回false"	
fi

if [[ $a -lt 100 || $b -gt 100 ]]; 
then
	echo "返回true"
else
	echo "返回false"	
fi