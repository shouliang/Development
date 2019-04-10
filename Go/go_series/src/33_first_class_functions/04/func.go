// 高阶函数02：在其他函数中 返回函数
package main

import "fmt"

// 在其他函数中 返回函数，函数返回类型是一个函数，此例中返回类型为func(a, b int) int
func simple() func(a, b int) int {
	f := func(a, b int) int {
		return a + b
	}
	return f
}

func main() {
	f := simple()
	fmt.Println(f(60, 8))
}
