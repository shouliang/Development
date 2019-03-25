// 共享内存并发机制
package share_mem

import (
	"sync"
	"testing"
	"time"
)

func TestCounter(t *testing.T) {
	counter := 0

	for i := 0; i < 5000; i++ {

		go func() {
			counter++
		}()

	}

	time.Sleep(1 * time.Second)    // 强制主进程休眠1秒来等待前面的5000goroutine
	t.Logf("counter =%d", counter) // counter在不同的协程里面自增，导致了竞争的并发条件，最终结果不是5000，线程不安全
}

func TestCounterThreadSafe(t *testing.T) {
	var mut sync.Mutex // 引入互斥锁
	counter := 0

	for i := 0; i < 5000; i++ {

		go func() {
			mut.Lock() // 加锁，线程安全
			counter++

			defer func() { // defer 相当于finally
				mut.Unlock() // 释放锁
			}()
		}()

	}

	// 强制sleep一秒等待前面的协程结束，再打印上counter,注释掉词句，很可能前面的5000个goroutin还没运行完，主进程已运行完毕，导致最终counter也没到5000
	time.Sleep(1 * time.Second)
	t.Logf("counter =%d", counter)
}

func TestCounterWaitGroup(t *testing.T) {
	var mut sync.Mutex    // 引入互斥锁
	var wg sync.WaitGroup // 引入WaitGroup
	counter := 0

	for i := 0; i < 5000; i++ {
		wg.Add(1) // 增加要等待的量

		go func() {
			mut.Lock() // 加锁，线程安全
			counter++
			wg.Done() // 主动告知WaitGroup任务完成

			defer func() { // defer 相当于finally
				mut.Unlock() // 释放锁
			}()
		}()
	}

	wg.Wait() // 在外层阻塞，等待所有任务完成
	t.Logf("counter =%d", counter)
}
