// 自定义函数类型的变量
package main

import "fmt"

// 正如我们定义自己的结构体类型一样，我们可以定义自己的函数类型
type add func(a int, b int) int

func main() {
	// 定义一个add类型的变量myadd，并赋值一个符合 add类型签名的函数
	var myadd add = func(a int, b int) int {
		return a + b
	}

	// 调用myadd函数
	s := myadd(5, 6)
	fmt.Println("Sum", s)
}
