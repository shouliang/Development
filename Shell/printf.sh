printf "Hello, Shell\n"

printf "%-10s %-8s %-4s\n" 姓名 性别 体重KG
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234
printf "%-10s %-8s %-4.2f\n" 杨过 男 66.1234
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876


printf "%d %s\n" 1 "abc"
printf '%d %s\n' 1 "abc"

printf %s abcdef
printf %s abc def
printf "%s %s %s\n" a b c d e f g h i j
printf "%s and %d \n"

printf "a string, no processing:<%s>\n" "A\nB"

printf "a string, no processing:<%b>\n" "A\nB"

printf "www.runoob.com \a"
