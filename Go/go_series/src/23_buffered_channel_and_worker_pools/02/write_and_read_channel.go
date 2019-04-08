package main

import (
	"fmt"
	"time"
)

// 向channel写入数据，满则阻塞
func write(ch chan int) {
	for i := 0; i < 5; i++ {
		ch <- i
		fmt.Println("successfully wrote", i, "to ch")
	}

	// 通道发送者主动关闭
	close(ch)
}

// 主进程从channel读取数据，空则阻塞
func main() {
	ch := make(chan int, 2)
	go write(ch)

	time.Sleep(2 * time.Second)

	for v := range ch {
		fmt.Println("read value", v, "from ch")
		time.Sleep(2 * time.Second)
	}
}
