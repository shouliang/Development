// 管道channel
/*
	channel是有类型的管道，可以用channel操作符 <- 对其发送或者接受值
	"箭头"就是数据流的方向
	ch <- v    // 将 v 送入 channel ch
	v := <-ch  // 从ch 接收，并赋值给 v

	默认情况下，在另一端准备好之前，发送和接收都会阻塞，这使得goroutine可以在没有明确的锁或竞态变量的情况下进行同步
*/
package main

import "fmt"

func sum(a []int, c chan int) {
	sum := 0
	for _, v := range a {
		sum += v
	}

	c <- sum // 将sum送入c
}

func main() {
	a := []int{7, 2, 8, -9, 4, 0}

	c := make(chan int) // make函数创建channel
	go sum(a[:len(a)/2], c)
	go sum(a[len(a)/2:], c)
	x, y := <-c, <-c // 从c中获取数据

	fmt.Println(x, y, x+y)
}
