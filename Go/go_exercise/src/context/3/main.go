// 使用Context：创建可取消的context，并取消goroutine
package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	// context.Background()返回一个空的Context,一般用于整个context树的根节点
	// context.WithCancle(parent),创建一个可取消的子context
	ctx, cancel := context.WithCancel(context.Background())

	go func(ctx context.Context) {
		for {
			select {
			case <-ctx.Done(): // 判断是否结束
				fmt.Println("监控退出...")
				return
			default:
				fmt.Println("goroutine监控中...")
				time.Sleep(2 * time.Second)
			}
		}
	}(ctx)

	time.Sleep(10 * time.Second)
	fmt.Println("开始通知监控停止")
	cancel() // cancel()函数取消指令，监控的goroutine就会收到信号

	time.Sleep(5 * time.Second)
}
