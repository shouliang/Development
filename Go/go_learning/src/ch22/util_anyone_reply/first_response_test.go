package util_any_reply

import (
	"fmt"
	"runtime"
	"testing"
	"time"
)

func runTask(id int) string {
	time.Sleep(10 * time.Millisecond)
	return fmt.Sprintf("The result is from %d", id)
}

func FirstResponse() string {
	numOfRunner := 10
	// ch := make(chan string) // 无缓冲
	ch := make(chan string, numOfRunner) // 有缓冲，防止协程泄露
	for i := 0; i < numOfRunner; i++ {
		go func(i int) {
			ret := runTask(i)
			ch <- ret
		}(i)
	}
	return <-ch // 只要有一个任务完成就返回
}

func TestFirstResponse(t *testing.T) {
	t.Log("Before:", runtime.NumGoroutine()) // 当前的协程数
	t.Log(FirstResponse())

	time.Sleep(1 * time.Second)
	t.Log("After:", runtime.NumGoroutine())
}
