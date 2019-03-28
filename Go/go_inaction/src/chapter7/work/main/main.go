// 展示如何使用work包创建一个goroutine池并完成工作
package main

import (
	"chapter7/work"
	"log"
	"sync"
	"time"
)

var names = []string{
	"steve",
	"bob",
	"mary",
	// "therese",
	// "jason",
}

// 定义namePrinter
type namePrinter struct {
	name string
}

// namePrinter实现Worker接口
func (m *namePrinter) Task() {
	log.Println(m.name)
	time.Sleep(time.Second)
}

func main() {
	// 创建工作池，初始化2个goroutine
	p := work.New(2)

	// 声明一个WaitGroup并初始化为要执行任务的goroutine数
	var wg sync.WaitGroup
	wg.Add(10 * len(names))

	// 循环将多个任务提交到工作池
	for i := 0; i < 10; i++ {
		for _, name := range names {
			np := namePrinter{
				name: name,
			}

			go func() {
				p.Run(&np)
				wg.Done()
			}()
		}
	}

	wg.Wait()

	p.Shutdown()

}
