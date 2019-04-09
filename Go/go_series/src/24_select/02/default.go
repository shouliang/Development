// select default
// 在没有 case 准备就绪时，可以执行 select 语句中的默认情况（Default Case）。
// 这通常用于防止 select 语句一直阻塞。
package main

import (
	"fmt"
	"time"
)

func process(ch chan string) {
	time.Sleep(10500 * time.Millisecond)
	ch <- "process successful"
}

func main() {
	ch := make(chan string)
	go process(ch)

	// 无限循环
	for {
		time.Sleep(1000 * time.Millisecond)
		select {
		case v := <-ch:
			fmt.Println("received value:", v)
			return
		default:
			fmt.Println("no value received")
		}
	}
}
