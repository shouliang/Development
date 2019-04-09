#!/bin/bash
# 变量
# 注意变量和等号之间不能由空格
your_name="tianya"

# 使用一个定义过的变量，只要在变量名前面加上美元符($)即可
# 但是推荐使用变量名外面加花括号的形式，即${变量名}
echo $your_name
echo ${your_name}

myUrl="http://google.com"

# 只读变量的值不能改变
readonly myUrl
myUrl="http://www.runoob.com"
