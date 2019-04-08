// 通道的发送与接收默认是阻塞的
package main

import "fmt"

func hello(done chan bool) {
	fmt.Println("Hello world goroutine")

	// 发送消息到通道done,解除主进程的阻塞
	done <- true
}

func main() {
	done := make(chan bool)
	go hello(done)

	// 主进程读取通道done,在此阻塞，除非向通道发送信息
	<-done
	fmt.Println("main function")
}
