package cancel_by_context // 关联任务的取消

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
	ctx, cancel := context.WithCancel(context.Background()) // ctx为当前根Context的子Context

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

	cancel()
	time.Sleep(time.Second * 1)
}
