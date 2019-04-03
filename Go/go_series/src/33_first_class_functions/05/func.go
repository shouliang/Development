// 闭包
package main

import "fmt"

// 当一个匿名函数所访问的变量定义在函数体的外部时，就称这样的匿名函数为闭包。
func main() {
	a := 5
	func() {
		fmt.Println("a =", a)
	}()
}
