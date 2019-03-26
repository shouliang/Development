// 展示如何使用互斥锁定义一段需要同步访问的代码临界区和资源的同步访问
package main

import (
	"fmt"
	"runtime"
	"sync"
)

var (
	counter int

	wg sync.WaitGroup

	// 互斥锁，用来定义一段代码临界区
	mutex sync.Mutex
)

func main() {
	wg.Add(2)

	go incCounter(1)
	go incCounter(2)

	wg.Wait()
	fmt.Printf("Final Counter:%d\n", counter)
}

//  使用互斥锁来同步并保证安全访问
func incCounter(id int) {
	defer wg.Done()

	for count := 0; count < 2; count++ {
		// 同一时刻只允许一个goroutine进入临界区
		// 加锁
		mutex.Lock()
		{
			value := counter
			runtime.Gosched()
			value++
			counter = value
		}
		// 释放锁，允许正在等待的goroutine进入临界区
		mutex.Unlock()
	}
}
