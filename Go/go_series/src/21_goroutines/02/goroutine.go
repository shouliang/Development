// 启动多个Go协程
package main

import (
	"fmt"
	"time"
)

// 打印 1-5
func numbers() {
	for i := 1; i <= 5; i++ {
		time.Sleep(250 * time.Millisecond)
		fmt.Printf("%d", i)
	}
}

// 打印 a-e
func alphabets() {
	for i := 'a'; i <= 'e'; i++ {
		time.Sleep(400 * time.Millisecond)
		fmt.Printf("%c", i)
	}
}

// 启动2个goroutine,会并发运行，所以会交替打印
func main() {
	go numbers()
	go alphabets()

	// 通过休眠，主进程等待前面2个协程结束
	time.Sleep(3000 * time.Millisecond)
	fmt.Printf("\nmain terminated\n")
}
