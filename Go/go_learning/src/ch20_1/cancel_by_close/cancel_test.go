package cancel_by_close // 任务的取消

import (
	"fmt"
	"testing"
	"time"
)

func isCancelled(cancelChan chan struct{}) bool {
	select {
	case <-cancelChan: // 从channel上收到消息，取消channel
		return true
	default:
		return false
	}
}

func cancel_1(cancelChan chan struct{}) {
	cancelChan <- struct{}{} // 空结构，发消息，只能取消一个任务
}

func cancel_2(cancelChan chan struct{}) {
	close(cancelChan) // 关闭channel,具有广播机制,全部取消
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

	// cancel_1(cancelChan)  // 只能取消掉一个协程goroutine
	cancel_2(cancelChan)
	time.Sleep(time.Second * 1)
}
