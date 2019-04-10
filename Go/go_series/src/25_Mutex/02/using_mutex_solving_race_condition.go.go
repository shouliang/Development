// 使用Mutex 解决竞争条件: 将临界区包裹在mutex.Lock 与 mutex.Unlock之间
package main

import (
	"fmt"
	"sync"
)

var x = 0

func increment(wg *sync.WaitGroup, mutex *sync.Mutex) {
	// 包裹在Lock和Unlock之间
	mutex.Lock()
	x = x + 1
	mutex.Unlock()

	wg.Done()
}

func main() {
	var wg sync.WaitGroup
	var mutex sync.Mutex
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go increment(&wg, &mutex)
	}

	wg.Wait()

	// 最终结果1000
	fmt.Println("final value of x", x)
}
