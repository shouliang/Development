// 高阶函数01：把函数作为参数，传递给其它函数
package main

import "fmt"

// 把函数作为参数，传递给其它函数
// a是是一个函数类型，函数签名为func(a, b int) int
func simple(a func(a, b int) int) {
	fmt.Println(a(60, 8))
}

func main() {
	// 创建一个匿名函数赋值给变量f,函数的签名符合simple函数的参数
	f := func(a, b int) int {
		return a + b
	}

	// 传递f到simple，并调用
	simple(f)
}
