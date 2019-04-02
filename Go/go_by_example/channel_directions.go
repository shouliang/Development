package main

import "fmt"

func ping(pings chan<- string, msg string) {
	pings <- msg
}

// chan<- 只允许发送数据到通道
// <-chan 只允许从通道接收数据
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}
