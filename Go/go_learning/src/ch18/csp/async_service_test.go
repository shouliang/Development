//CSP模式通过Channel进行通讯，channel是有容量限制并独立于处理Goroutine
package csp

import (
	"fmt"
	"testing"
	"time"
)

func service() string {
	// time.Sleep(time.Millisecond * 50)
	time.Sleep(time.Millisecond * 500)
	return "service Done"
}

func otherTask() {
	fmt.Println("working on otherTask")
	time.Sleep(time.Microsecond * 100)
	fmt.Println("otherTask is done")
}

// func TestService(t *testing.T) {
// 	fmt.Println(service())
// 	otherTask()
// }

func AsyncService() chan string {
	// retCh := make(chan string)
	retCh := make(chan string, 1)
	go func() {
		ret := service()
		fmt.Println("returned result.")
		retCh <- ret
		fmt.Println("service exited.")
	}()

	return retCh
}

func TestAsyncService(t *testing.T) {
	retCh := AsyncService()

	otherTask()

	fmt.Println(<-retCh)
	time.Sleep(time.Second * 1)
}

// 多路选择
func TestSelect(t *testing.T) {
	select {
	case ret := <-AsyncService():
		t.Log(ret)
	case <-time.After(time.Millisecond * 100): // 超时控制，防止阻塞主进程
		t.Error("time out")
	}
}
