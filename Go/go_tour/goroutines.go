// goroutine
/*
goroutine 是由Go运行时环境管理的轻量级线程
go f(x,y,z) 开启一个新的goroutine执行
*/

package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		time.Sleep(100 * time.Microsecond)
		fmt.Println(s)
	}
}

func main() {
	// 同步运行
	say("hello")
	say("world")

	// 加go关键字，函数就运行在一个goroutin里面了，就变成异步执行了
	fmt.Println("----------goroutine----------")
	go say("hello")
	go say("world")

	// main所处的进程强制等待一秒，等待前面的2个 go
	time.Sleep(time.Second * 1)
}
