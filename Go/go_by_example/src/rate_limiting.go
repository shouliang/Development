package main

import (
	"fmt"
	"time"
)

func main() {
	// requests := make(chan int, 5)
	// for i := 1; i <= 5; i++ {
	// 	requests <- i
	// }
	// close(requests)
	//
	// limiter := time.Tick(time.Millisecond * 200)
	//
	// for req := range requests {
	// 	// 通过在每次请求前阻塞 limiter 通道的一个接收，我们限制自己每 200ms 执行一次请求。
	// 	<-limiter
	// 	fmt.Println("request", req, time.Now())
	// }

	// burstyLimiter 通道用来进行 3 次临时的脉冲型速率限制。
	burstyLimiter := make(chan time.Time, 3)
	for i := 0; i < 3; i++ {
		burstyLimiter <- time.Now()
	}

	go func() {
		for t := range time.Tick(time.Millisecond * 200) {
			burstyLimiter <- t
		}
	}()

	burstyRequests := make(chan int, 5)
	for i := 1; i <= 5; i++ {
		burstyRequests <- i
	}
	close(burstyRequests)

	// 现在模拟超过 5 个的接入请求。它们中刚开始的 3 个将由于受 burstyLimiter 的“脉冲”影响。
	// 第二批请求，我们直接连续处理了 3 次，这是由于这个“脉冲”速率控制，然后大约每 200ms 处理其余的 2 个。
	for req := range burstyRequests {
		<-burstyLimiter
		fmt.Println("request", req, time.Now())
	}

}
