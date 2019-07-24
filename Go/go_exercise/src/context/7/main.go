// 截止时间 取消 context.WithDeadline
package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	d := time.Now().Add(1 * time.Second)
	ctx, cancle := context.WithDeadline(context.Background(), d)

	defer cancle()

	select {
	case <-time.After(2 * time.Second):
		fmt.Println("oversleep")
	case <-ctx.Done():
		fmt.Println(ctx.Err())
	}
}
