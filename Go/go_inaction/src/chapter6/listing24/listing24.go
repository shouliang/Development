// 展示如何使用有缓冲的通道和固定数目的goroutine来处理一堆工作
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

const (
	numberGoroutines = 4  // 要使用的goroutine的数量
	taskLoad         = 10 // 要处理的工作的数量
)

var wg sync.WaitGroup

func init() {
	// 初始化随机数种子
	rand.Seed(time.Now().Unix())
}

func main() {
	// 创建一个有缓冲的通道来管理工作
	tasks := make(chan string, taskLoad)

	wg.Add(numberGoroutines)

	// 启动goroutine来处理工作
	for gr := 1; gr <= numberGoroutines; gr++ {
		go worker(tasks, gr)
	}

	// 增加一组要完成的工作
	for post := 1; post <= taskLoad; post++ {
		tasks <- fmt.Sprintf("Task : %d", post)
	}

	// 当所有工作都处理完时关闭通道
	// 以便所有goroutine退出
	close(tasks)

	wg.Wait()
}

// 处理从有缓冲的通道传入的工作
func worker(tasks chan string, work int) {
	defer wg.Done()

	for {
		// 等待分配工作
		task, ok := <-tasks
		if !ok {
			// 这意味着通道已经空了，并且也被关闭
			fmt.Printf("Worker: %d : Shutting Down\n", worker)
			return
		}

		// 打印出我们开始工作
		fmt.Printf("Worker: %d : Started %s\n", worker, task)

		// 随机等一段时间来模拟工作
		sleep := rand.Int63n(100)
		time.Sleep(time.Duration(sleep) * time.Millisecond)

		// 打印出工作完成
		fmt.Printf("Worker: %d : Completed %s\n", worker, task)
	}
}
