package main

import (
	"fmt"
	"sync"
	"time"
)

var (
	wakeup    = false
	workerNum = 3
)

func worker(workID int, c *sync.Cond) {
	fmt.Printf("Worker [%d] is RUNNING\n", workID)
	c.L.Lock()

	for !wakeup {
		fmt.Printf("Worker [%d] check condition\n", workID)
		c.Wait()
	}
	fmt.Printf("Worker [%d] wakeup, Do something\n", workID)

	// 将唤醒标志改为false
	// 此时其他已经醒来并抢夺互斥锁的goroutine重新判断条件后，将再次进入wait状态
	wakeup = false
	c.L.Unlock()
}

func main() {
	cond := sync.NewCond(&sync.Mutex{})
	for i := 0; i < workerNum; i++ {
		go worker(i, cond)
	}

	time.Sleep(2 * time.Second)
	wakeup = true

	// 向所有goroutine进行广播，条件已经满足，即wakeup = true
	cond.Broadcast()

	time.Sleep(2 * time.Second)

	// 当 worker0 醒来后，又重新把条件变量进行了修改，
	// 从而导致 worker1 和 worker2 获取到互斥锁后重新检查到条件不满足，再次进入 wait 状态。
}
