// 通道同步
package main

import (
	"fmt"
	"time"
)

func worker(done chan bool) {
	fmt.Println("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	// 通知主进程本协程已经工作完毕
	done <- true
}

func main() {
	done := make(chan bool, 1)
	go worker(done)

	fmt.Println("waiting worker working...")

	// 主进程将在接收到通道中发出的通知前一直阻塞
	<-done
}
