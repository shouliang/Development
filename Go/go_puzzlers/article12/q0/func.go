// 函数可以作为普通的值
// 在其他函数间传递、赋予变量、做类型判断和转换
package main

import "fmt"

// 自定义一个函数类型，名称为Printer
type Printer func(contents string) (n int, err error)

func printToStd(contents string) (bytesNum int, err error) {
	return fmt.Println(contents)
}

func main() {
	var p Printer

	// 两个函数的参数列表和结果列表中的元素顺序及其类型是一致的
	// 则它们是一样的函数
	// 将函数printToStd赋值给函数p
	p = printToStd
	p("something")
}
