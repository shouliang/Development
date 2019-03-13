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
	go say("hello")
	say("world")
}
