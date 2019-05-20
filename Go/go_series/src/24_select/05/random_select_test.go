// 随机选择:当 select 由多个 case 准备就绪时，将会随机地选取其中之一去执行。
package main

import (
	"testing"
	"time"
)

func server1(ch chan string) {
	ch <- "from server1"
}

func server2(ch chan string) {
	ch <- "from server2"
}

func TestRandomSelect(t *testing.T) {
	output1 := make(chan string)
	output2 := make(chan string)

	go server1(output1)
	go server2(output2)

	time.Sleep(1 * time.Second)
	select {
	case s1 := <-output1:
		t.Log(s1)
	case s2 := <-output2:
		t.Log(s2)
	}
}
