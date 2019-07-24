// Context控制多个goroutine
package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, cancle := context.WithCancel(context.Background())

	// 每一个goroutine，都使用context进行跟踪
	go watch(ctx, "【监控1】")
	go watch(ctx, "【监控2】")
	go watch(ctx, "【监控3】")

	time.Sleep(10 * time.Second)
	fmt.Println("开始通知监控停止...")

	cancle()
	time.Sleep(5 * time.Second)
}

func watch(ctx context.Context, name string) {
	for {
		select {
		case <-ctx.Done():
			fmt.Println(name, "监控退出...")
			return
		default:
			fmt.Println(name, "goroutine监控中...")
			time.Sleep(2 * time.Second)
		}
	}
}
