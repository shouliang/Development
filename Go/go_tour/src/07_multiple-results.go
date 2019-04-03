// 多值返回
package main

import "fmt"

// swap函数返回了两个字符串
func swap(x, y string) (string, string) {
	return y, x
}

func main() {
	a, b := swap("hello", "world")
	fmt.Println(a, b)
}
