// 短声明变量
package main

import "fmt"

// 在函数内，`:=`简洁赋值语句，不能使用在函数外
// 函数外的每个语句都必须以关键字开始( var、func等)
func main() {
	var i, j int = 1, 2
	k := 3
	c, python, java := true, false, "no!"

	fmt.Println(i, j, k, c, python, java)
}
