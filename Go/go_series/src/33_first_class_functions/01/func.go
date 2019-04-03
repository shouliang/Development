// First Class Function
// 可以把函数赋值给变量，也可以把函数作为其它函数的参数或者返回值。
// Go 语言支持头等函数的机制。
package main

import "fmt"

func main() {
	// 将一个匿名函数赋值给变量a
	a := func() {
		fmt.Println("hello world first class function")
	}

	// 调用函数
	a()

	// 打印出变量a的类型为 func()
	fmt.Printf("%T\n", a)

	// 匿名函数：不需要赋值给一个变量，可立即执行
	func() {
		fmt.Println("anonymous function without assigning it to a variable")
	}()

	// 匿名函数：传递参数
	func(name string) {
		fmt.Println("Welcome", name)
	}("Gophers")

}
