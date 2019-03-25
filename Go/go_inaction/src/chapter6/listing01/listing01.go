// goroutine调度器如何在单个线程上切分时间片
package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	// Allocate 1 logical processor
	// 1个逻辑处理器，CPU时间片切换
	//runtime.GOMAXPROCS(1)
	// 2个逻辑处理器，goroutine是真正的同时运行，而不是CPU时间片切换
	//runtime.GOMAXPROCS(2)
	numCPU := runtime.NumCPU()
	fmt.Println("NumCPU is", numCPU)
	runtime.GOMAXPROCS(runtime.NumCPU())

	// wg is used to wait for the program to finish
	// Add a count of three, one for each goroutine
	var wg sync.WaitGroup
	wg.Add(3)

	fmt.Println("Start Goroutines")

	// go关键字后声明一个匿名函数来运行一个goroutine
	go func() {
		// Schedule the call to Done to tell main we are done
		defer wg.Done()

		for count := 0; count < 3; count++ {
			for char := 'a'; char < 'a'+26; char++ {
				fmt.Printf("%c", char)
			}
		}
	}()

	go func() {
		defer wg.Done()

		fmt.Printf("\njust add one short goroutine\n")
	}()

	go func() {
		defer wg.Done()

		// Dispaly the alphebet three times
		for count := 0; count < 3; count++ {
			for char := 'A'; char < 'A'+26; char++ {
				fmt.Printf("%c", char)
			}
		}
	}()

	// 等待goroutines结束
	// 各个goroutine是并发执行的，而不是按照代码编写的顺序
	fmt.Println("Waiting to Finish")
	wg.Wait()

	fmt.Printf("\nTerminating Program")
}
