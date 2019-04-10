// 闭包:每一个闭包都会绑定一个它自己的外围变量（Surrounding Variable）
package main

import "fmt"

func appendStr() func(string) string {
	t := "Hello"

	c := func(b string) string {
		// 内部函数使用了外部函数的变量t
		t = t + " " + b
		return t
	}

	// 返回了一个闭包，闭包是一个函数
	return c
}

func main() {
	// 变量a、b都是闭包，它们绑定了各自的t值
	a := appendStr()
	b := appendStr()

	fmt.Println(a("World"))
	fmt.Println(b("Everyone"))

	fmt.Println(a("Gopher"))
	fmt.Println(b("!"))

}
