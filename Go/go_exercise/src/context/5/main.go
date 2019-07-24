// WithValue传递元数据
package main

import (
	"context"
	"fmt"
	"time"
)

var key string = "name"

func main() {
	ctx, cancle := context.WithCancel(context.Background())

	// 赋值，用于传递
	valueCtx := context.WithValue(ctx, key, "【监控1】")
	go watch(valueCtx)

	time.Sleep(10 * time.Second)
	fmt.Println("开始停止监控...")
	cancle()

	time.Sleep(5 * time.Second)
}

func watch(ctx context.Context) {
	for {
		select {
		case <-ctx.Done():
			// 取出值
			fmt.Println(ctx.Value(key), "监控退出...")
			return
		default:
			fmt.Println(ctx.Value(key), "goroutine监控中...")
			time.Sleep(2 * time.Second)
		}
	}
}
