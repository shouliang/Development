// select 语句用于在多个发送/接收通道操作中进行选择。
// select 语句会一直阻塞，直到发送/接收操作准备就绪。
// 如果有多个通道操作准备完毕，select 会随机地选取其中之一执行。
package main

import (
	"testing"
	"time"
)

func server1(ch chan string) {
	time.Sleep(6 * time.Second)
	ch <- "from server1"
}

func server2(ch chan string) {
	time.Sleep(3 * time.Second)
	ch <- "from server2"
}

func TestSelect(t *testing.T) {
	output1 := make(chan string)
	output2 := make(chan string)

	go server1(output1)
	go server2(output2)

	select {
	case s1 := <-output1:
		t.Log(s1)
	case s2 := <-output2:
		t.Log(s2)
	}
}
