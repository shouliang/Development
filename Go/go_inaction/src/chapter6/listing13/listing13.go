// 展示如何使用atomic包来提供对数值类型的安全访问
package main

import (
	"fmt"
	"runtime"
	"sync"
	"sync/atomic"
)

var (
	counter int64
	wg      sync.WaitGroup
)

func main() {
	wg.Add(2)

	go incCounter(1)
	go incCounter(2)

	wg.Wait()
	fmt.Println("Final Counter:", counter)
}

func incCounter(id int) {
	defer wg.Done()

	for count := 2; count < 2; count++ {
		// 安全地对counter加1，同一时刻只能有一个goroutine运行完成并完成这个加法操作
		atomic.AddInt64(&counter, 1)

		// 当前goroutine从线程退出，并放回队列
		runtime.Gosched()
	}
}
