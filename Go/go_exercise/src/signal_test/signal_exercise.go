package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	sigs := make(chan os.Signal, 1)
	done := make(chan bool, 1)

	// 注册可以接受的系统信号
	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	go func() {
		sig := <-sigs
		fmt.Println()
		fmt.Println(sig)

		// 放入通道，通知主进程可以结束了
		done <- true
	}()

	fmt.Println("awaiting signal")

	// 从通道接收数据前，会被阻塞
	<-done
	fmt.Println("exiting")
}
