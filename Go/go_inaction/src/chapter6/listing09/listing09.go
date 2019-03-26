// 展示如何在程序中造成竞争状态
package main

import (
	"fmt"
	"runtime"
	"sync"
)

var (
	// counter是所有goroutine都要增加其值的变量
	counter int

	// wg用来等待程序结束
	wg sync.WaitGroup
)

func main() {
	// 计数器加2，表示要等待的2个goroutine
	wg.Add(2)

	// 创建2个goroutine
	go incCounter(1)
	go incCounter(2)

	// 等待goroutine结束
	wg.Wait()
	fmt.Println("Final Counter:", counter)
}

// 增加包变量counter的值，但是是线程不安全的
func incCounter(id int) {
	defer wg.Done()

	for count := 0; count < 2; count++ {
		// 每个goroutine创建一个counter变量的副本
		value := counter

		// 强制调度器切换到另一个goroutine
		// 当前goroutine从线程退出，并放回到队列
		runtime.Gosched()

		//运行到此处，可能counter已经被另外一个goroutine改变了，但是goroutine还是继续使用当前副本的值，自增后存回counter,从而覆盖了另外一个goroutine完成的工作
		value++

		counter = value
	}
}
