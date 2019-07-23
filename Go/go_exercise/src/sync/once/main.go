// sync.Once(f), function f只会触发一次
package main

import (
	"fmt"
	"sync"
)

func main() {
	var once sync.Once
	onceBody := func() {
		fmt.Println("Only once")
	}

	done := make(chan bool)

	// 创建10个goroutine，但是onceBody只执行1次
	for i := 0; i < 10; i++ {
		go func() {
			once.Do(onceBody)
			done <- true
		}()
	}

	// 等待10个goroutine结束
	for i := 0; i < 10; i++ {
		<-done
	}
}
