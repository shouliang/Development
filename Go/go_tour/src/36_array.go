// 数组
/*
	类型 [n]T 是一个有n个类型为T的值的数组
	表达式 var a [10]int 定义变量a是一个10个int类型的数组
	数组长度是其类型的一部分，不能改变其大小
*/
package main

import "fmt"

func main() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)
}
