// 关联任务的取消
package cancel_by_context

import (
	"context"
	"fmt"
	"testing"
	"time"
)

func isCancelled(ctx context.Context) bool {
	select {
	case <-ctx.Done(): // context是否完成
		return true
	default:
		return false
	}
}

// 根Context:通过context.Background()创建
// 子Context: context.WithCancel(parentContext)创建
//	ctx, cancel := context.WithCancel(context.Background())
// 当前Context被取消时，基于他的子context都会被取消
// 任务取消  发消息取消
func TestCancel(t *testing.T) {
	// ctx为当前根Context的子Context
	ctx, cancel := context.WithCancel(context.Background())

	for i := 0; i < 5; i++ {
		go func(i int, ctx context.Context) {
			for {
				if isCancelled(ctx) {
					break
				}
				time.Sleep(time.Millisecond * 5)
			}
			fmt.Println(i, "Done")
		}(i, ctx)
	}

	// 调用cancel()函数
	cancel()
	time.Sleep(time.Second * 1)
}
