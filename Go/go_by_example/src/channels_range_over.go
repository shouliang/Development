package main

import "fmt"

func main() {
	queue := make(chan string, 2)
	queue <- "one"
	queue <- "two"
	close(queue)

	// 一个非空的通道也是可以关闭的，但是通道中剩下的值仍然可以被接收到。
	// 如果不关闭通道，将在这个循环中阻塞执行，等待接收第三个值
	for elem := range queue {
		fmt.Println(elem)
	}
}
