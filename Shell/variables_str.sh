your_name="runoob"

greeting="hello, "$your_name" !"
greeting_1="hello,${your_name} !"
echo $greeting $greeting_1

greeting_2='hello,'$your_name''
greeting_3='hello,${your_name}'
echo $greeting_2 $greeting_3

string="abcd"
echo ${#string}

string="runoob is a great site"
echo ${string:1:4}

string="runoob is a great site"
echo `expr index "$string" io`
