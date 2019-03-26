// 展示如何用无缓冲的通道来模拟2个goroutine间的网球比赛
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

	// 开始发球
	court <- 1

	// 等待游戏结束
	wg.Wait()
}

func player(name string, court chan int) {
	defer wg.Done()

	for {
		// 等待球被击打过来,会锁住goroutine直到有数据发送到通道里
		ball, ok := <-court
		if !ok {
			// 如果通道关闭，我们就赢了，游戏结束
			fmt.Printf("Player %s Won\n", name)
			return
		}

		// 选随机数，然后用这个数判断是否丢球，然后关闭通道
		n := rand.Intn(100)
		if n%13 == 0 {
			fmt.Printf("Player %s Missed\n", name)

			// 关闭通道，表示我们输了
			close(court)
			return
		}

		fmt.Printf("Player %s Hint %d\n", name, ball)
		ball++

		// 将球重新放入通道，发送给另外一个选手
		court <- ball
	}
}
