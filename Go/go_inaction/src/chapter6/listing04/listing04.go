// 如何创建goroutine以及goroutine调度器的行为
package main

import (
	"fmt"
	"runtime"
	"sync"
)

var wg sync.WaitGroup

func main() {
	// 一个逻辑处理器，两个goroutine会来回切换，但是实际的看的可能是一个已经执行完毕，而后切换到另外一个，而不是来回切换
	runtime.GOMAXPROCS(1)
	wg.Add(2)

	fmt.Println("Create Goroutines")
	go printPrime("A")
	go printPrime("B")

	fmt.Println("Wating To Finish")
	wg.Wait()
	fmt.Println("Terminating Program")
}

func printPrime(prefix string) {
	defer wg.Done()

	// 计算5000以内的素数
next:
	for outer := 2; outer < 5000; outer++ {
		for inner := 2; inner < outer; inner++ {
			if outer%inner == 0 {
				continue next
			}
		}
		fmt.Printf("%s:%d\n", prefix, outer)
	}
	fmt.Println("Completed", prefix)
}
