// 长度 vs 容量
package main

import "fmt"

func main() {
	ch := make(chan string, 3)
	ch <- "naveen"
	ch <- "paul"

	fmt.Println("capacity is", cap(ch)) // 3
	fmt.Println("length is", len(ch))   // 2
	fmt.Println("read value", <-ch)
	fmt.Println("new length is", len(ch)) // 1
}
