package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var wg sync.WaitGroup

func init() {
	rand.Seed(time.Now().UnixNano())
}

func main() {
	// 创建一个无缓冲的channel
	court := make(chan int)

	wg.Add(2)

	go player("zhangsan", court)
	go player("lisi", court)

	// 开始击球
	court <- 1

	wg.Wait()
}

func player(name string, court chan int) {
	defer wg.Done()

	for {
		// Wait for the ball to be hit back to us
		ball, ok := <-court
		if !ok {
			// If the channel was closed we won
			fmt.Printf("Player %s Won\n", name)
			return
		}

		n := rand.Intn(100)
		if n%13 == 0 {
			fmt.Printf("Player %s Missed\n", name)

			// Close the channel to signal we lost
			close(court)
			return
		}

		fmt.Printf("Player %s Hint %d\n", name, ball)
		ball++

		court <- ball
	}
}
