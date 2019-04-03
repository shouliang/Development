// 实现自定的map函数
package main

import "fmt"

func iMap(s []int, f func(int) int) []int {
	var r []int
	// 将f(v)添加到新生成的切片
	for _, v := range s {
		r = append(r, f(v))
	}
	return r
}

func main() {
	a := []int{5, 6, 7, 8, 9}
	r := iMap(a, func(n int) int {
		return n * 5
	})

	fmt.Println(r)
}
