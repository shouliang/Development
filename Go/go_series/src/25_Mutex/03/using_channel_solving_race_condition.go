// 使用通道 解决竞争条件
package main

import (
	"fmt"
	"sync"
)

var x = 0

func increment(wg *sync.WaitGroup, chl chan bool) {
	// 由于缓冲通道的容量为 1，
	//所以任何其他协程试图写入该信道时，都会发生阻塞 ，直到 x 增加后，通道的值才会被读取
	chl <- true
	x = x + 1
	<-chl

	wg.Done()
}

func main() {
	var wg sync.WaitGroup
	chl := make(chan bool, 1)
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go increment(&wg, chl)
	}

	wg.Wait()
	fmt.Println("final value of x", x)
}
