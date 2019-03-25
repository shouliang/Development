// 协程Goroutine的Stack的初始化大小为2k
// 和KSE(Kernel Space Entity)是 多对对 的关系，内核切换消耗小
// 一对一的关系 内核线程切换消耗大
// Process下挂载协程队列
package goroutine_test

import (
	"fmt"
	"testing"
	"time"
)

func TestGoroutine(t *testing.T) {
	for i := 0; i < 10; i++ {
		// 让函数在协程里面运行，函数前加go关键字即可
		go func(i int) {
			fmt.Println(i)
		}(i) // 函数传入的是i的副本

		// 以下这种方式会让go后面的协程，共享TestGoroutine函数里面的变量i,会产生竞争机制
		// 实际是还没等运行到go后面的匿名函数，主进程的for循环已经运行结束了
		// go func() {
		// 	fmt.Println(i)
		// }()
	}

	time.Sleep(time.Microsecond * 50)
}
