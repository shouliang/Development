// 在竞争转态不希望出现的状况
package main

import (
	"fmt"
	"runtime"
	"sync"
)

var (
	counter int
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

	for count := 0; count < 2; count++ {
		// 每个goroutine创建一个counter变量的副本
		value := counter

		// 强制调度器切换到另一个goroutine
		runtime.Gosched()

		//运行到此处，可能counter已经被另外一个goroutine改变了，但是goroutine还是继续使用当前副本的值，自增后存回counter,从而覆盖了另外一个goroutine完成的工作
		value++

		counter = value
	}
}
