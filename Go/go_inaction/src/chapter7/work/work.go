package work

import "sync"

// Worker接口，必须满足接口类型才能使用工作池
type Worker interface {
	Task()
}

// 定义一个goroutine工作池，可以完成任何已提交的Worker任务
type Pool struct {
	// Worker接口类型的通道
	work chan Worker
	wg   sync.WaitGroup
}

// 创建一个新工作池
func New(maxGoroutines int) *Pool {
	p := Pool{
		work: make(chan Worker),
	}

	p.wg.Add(maxGoroutines)

	for i := 0; i < maxGoroutines; i++ {
		go func() {
			// 阻塞住，直到work通道收到一个Worker接口值
			for w := range p.work {
				w.Task()
			}
			p.wg.Done()
		}()
	}

	return &p
}

// 提交工作到工作池
func (p *Pool) Run(w Worker) {
	p.work <- w
}

// 等待所有goroutine停止工作
func (p *Pool) Shutdown() {
	// 关闭通道
	close(p.work)
	p.wg.Wait()
}
