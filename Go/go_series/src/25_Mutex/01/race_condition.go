//含有竞态条件的程序
package main

import (
	"fmt"
	"sync"
)

var x = 0

func increment(wg *sync.WaitGroup) {
	x = x + 1
	wg.Done()
}

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 1000; i++ {
		wg.Add(1)

		// 传递 wg 的地址是很重要的。
		// 如果没有传递 wg 的地址，那么每个 Go 协程将会得到一个 WaitGroup 值的拷贝，
		// 因而当它们执行结束时，main 函数并不会知道。
		go increment(&wg)
	}
	wg.Wait()

	// 最终的结果通常不会是1000
	fmt.Println("final value of x", x)
}
