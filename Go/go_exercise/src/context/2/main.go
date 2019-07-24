// channel + select 监控goroutine
// 定义全局的channel, 然后后台goroutine不停的检查这个channel,直到发现给通知关闭了
package main

import (
	"fmt"
	"time"
)

func main() {
	stop := make(chan bool)

	go func() {
		for {
			select {
			case <-stop:
				fmt.Println("监控退出...")
				return
			default:
				fmt.Println("goroutine监控中...")
				time.Sleep(2 * time.Second)
			}
		}
	}()

	time.Sleep(10 * time.Second)
	fmt.Println("开始通知监控停止")
	stop <- true

	time.Sleep(5 * time.Second)
}
