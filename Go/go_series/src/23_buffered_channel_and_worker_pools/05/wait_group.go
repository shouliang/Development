// WaitGroup: 用于等待一批 Go 协程执行结束。
// 程序控制会一直阻塞，直到这些协程全部执行完毕
package main

import (
	"fmt"
	"sync"
	"time"
)

func process(i int, wg *sync.WaitGroup) {
	fmt.Println("started Goroutine", i)
	time.Sleep(2 * time.Second)
	fmt.Printf("Goroutine %d ended\n", i)

	//Done():计数器减1
	wg.Done()
}

func main() {
	no := 3
	var wg sync.WaitGroup

	// 开启多个goroutine，并发执行
	for i := 0; i < no; i++ {

		// Add(1):计数器加1
		wg.Add(1)
		go process(i, &wg)
	}

	// Wait() 方法会阻塞调用它的 Go 协程
	// 直到计数器变为 0 后才会停止阻塞。
	wg.Wait()
	fmt.Println("All go routines finished executing")
}
