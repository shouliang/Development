// RWMutex的几条规则示例
package main

import (
	"fmt"
	"sync"
	"time"
)

var rw sync.RWMutex

func reader(readerID int) {
	fmt.Printf("[reader-%d] try to get read lock\n", readerID)
	rw.RLock()
	fmt.Printf("[reader-%d] get read lock and sleep\n", readerID)
	time.Sleep(1 * time.Second)
	fmt.Printf("[reader-%d] release read lock\n", readerID)
	rw.RUnlock()
}

func writer(writerID int) {
	fmt.Printf("[writer-%d] try to get write lock\n", writerID)
	rw.Lock()
	fmt.Printf("[writer-%d] get write lock and sleep\n", writerID)
	time.Sleep(3 * time.Second)
	fmt.Printf("[writer-%d] release write lock\n", writerID)
	rw.Unlock()
}

func main() {
	// 启动多个goroutine 获取read lock 后 sleep 一段时间
	// 由于此时没有写者，所以两个 reader 都可以同时获得读锁
	go reader(1)
	go reader(2)

	time.Sleep(500 * time.Millisecond)

	// 写者获取写锁，由于读锁未被释放，所以一开始写者获取不到写锁
	go writer(1)

	time.Sleep(1 * time.Second)

	// 由于写锁还未释放，新的读者获取不到读锁
	go reader(3)
	go reader(4)

	// 主goroutine 等待足够长时间让所有goroutine执行完
	time.Sleep(10 * time.Second)
}
