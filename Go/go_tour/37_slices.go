// slice
// 一个slice会指向一个序列的值，并且包含了长度信息
package main

import (
	"fmt"
)

func main() {
	p := []int{2, 3, 5, 7, 11, 13}
	fmt.Println("p ==", p)
	fmt.Println("len(p) ==", len(p))

	for i := 0; i < len(p); i++ {
		fmt.Printf("p[%d] == %d \n", i, p[i])
	}
}
