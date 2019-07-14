package cancel_by_close // 任务的取消

import (
	"fmt"
	"testing"
	"time"
)

func isCancelled(cancelChan chan struct{}) bool {
	select {
	// 从channel上收到消息，取消channel
	case <-cancelChan:
		return true
	default:
		return false
	}
}

func cancel_1(cancelChan chan struct{}) {
	// 空结构，发消息，只能取消一个任务
	cancelChan <- struct{}{}
}

func cancel_2(cancelChan chan struct{}) {
	// 关闭channel,具有广播机制,全部取消
	close(cancelChan)
}

// 任务取消  发消息取消
func TestCancel(t *testing.T) {
	cancelChan := make(chan struct{}, 0)
	for i := 0; i < 5; i++ {
		go func(i int, cancelCh chan struct{}) {
			for {
				if isCancelled(cancelCh) {
					break
				}
				time.Sleep(time.Millisecond * 5)
			}
			fmt.Println(i, "Done")
		}(i, cancelChan)
	}

	// 只能取消掉一个协程goroutine
	cancel_1(cancelChan)

	//cancel_2(cancelChan)
	time.Sleep(time.Second * 1)
}
