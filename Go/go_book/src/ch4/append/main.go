package main

import "fmt"

func main() {
	var x, y []int
	for i := 0; i < 10; i++ {
		y = appendInt(x, i)
		fmt.Printf("%d cap=%d\t%v\n", i, cap(y), y)
		x = y
	}
}

func appendInt(x []int, y int) []int {
	var z []int
	zlen := len(x) + 1 // 每次append，zlen新增1
	if zlen <= cap(x) {
		z = x[:zlen] // slice仍有增长空间
	} else {
		// slice无空间，分配一个新的底层数组,容量扩展一倍
		zcap := zlen
		if zcap < 2*len(x) {
			zcap = 2 * len(x)
		}
		z = make([]int, zlen, zcap)
		copy(z, x) // 使用内置的copy函数
	}
	z[len(x)] = y
	return z
}
