// 向slice中添加元素
/*
	内建函数append向slice添加元素
	append的结果是一个包含原slice的所有元素和新添加的元素的slice
	如果slice底层数组太小，会分配一个更大的数组，返回的slice会指向这个新分配的数组
*/
package main

import "fmt"

func main() {
	var a []int
	printSlice("a", a)

	a = append(a, 0)
	printSlice("a", a)

	a = append(a, 1)
	printSlice("a", a)

	a = append(a, 2, 3, 4) // 一次可以添加多个元素到slice
	printSlice("a", a)
}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n", s, len(x), cap(x), x)
}
