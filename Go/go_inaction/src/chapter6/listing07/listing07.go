// 展示如何创建goroutine以及调度器的行为
package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	// 分配2个逻辑处理器给调度器使用
	// 2个逻辑处理器，goroutine是真正的同时运行，而不是CPU时间片切换
	runtime.GOMAXPROCS(2)

	// wg 用来等待程序完成
	// 计数加2，表示要等待2个goroutine
	// WaitGroup是一个计数信号量，值大于0，Wait()方法就会阻塞
	var wg sync.WaitGroup
	wg.Add(2)

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
