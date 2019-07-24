// 超时取消 context.WithTimeout
package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

var wg sync.WaitGroup

func main() {
	// 4秒超时后，自动取消goroutine
	ctx, cancel := context.WithTimeout(context.Background(), 4*time.Second)
	defer cancel()

	fmt.Println("Hey,I'm going to do some work")
	wg.Add(1)
	go work(ctx)
	wg.Wait()
	fmt.Println("Finished. I'm going home")
}

func work(ctx context.Context) error {
	defer wg.Done()

	for i := 0; i < 1000; i++ {
		select {
		case <-time.After(1 * time.Second):
			fmt.Println("Doing some work", i)
		case <-ctx.Done():  // Done() 接收到取消信号
			fmt.Println("Cancle the context", i)
			return ctx.Err()
		}
	}

	return nil
}
