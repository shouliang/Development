// 展示如何使用atomic包里的Store和Load函数来提供对数值类型的安全访问
package main

import (
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

var (
	// shutdown是通知正在执行的goroutine停止工作的标志
	shutdown int64
	wg       sync.WaitGroup
)

func main() {
	wg.Add(2)

	go doWork("A")
	go doWork("B")

	time.Sleep(2 * time.Second)

	// 关闭运行中的goroutine
	fmt.Println("Shutdown Now")

	// 原子性第设置shutdonw变量
	atomic.StoreInt64(&shutdown, 1)

	wg.Wait()

}

func doWork(name string) {
	defer wg.Done()

	for {
		// 模拟dowork的运行，完毕后关闭
		fmt.Printf("Doing %s Work\n", name)
		time.Sleep(250 * time.Millisecond)

		// 原子性地载入shutdown变量
		if atomic.LoadInt64(&shutdown) == 1 {
			fmt.Printf("Shutting %s Down\n", name)
			break
		}
	}
}
