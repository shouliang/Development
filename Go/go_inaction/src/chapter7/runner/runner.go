// Package runner 包管理任务的运行和生命周期
package runner

import (
	"errors"
	"os"
	"os/signal"
	"time"
)

// 在给定的超时时间内执行一组任务
type Runner struct {
	// 操作系统信号类型的 通道
	interrupt chan os.Signal

	// error类型的通道 表示是否已经完成任务
	complete chan error

	// timeout 是只读类型的通道
	timeout <-chan time.Time

	// 要执行的任务函数切片
	tasks []func(int)
}

// 超时错误
var ErrTimeout = errors.New("received timeout")

// 操作系统(ctrl + c )中断错误
var ErrInterrupt = errors.New("received interrupt")

// 返回一个新的准备使用的Runner
func New(d time.Duration) *Runner {
	return &Runner{
		// 有缓冲通道
		interrupt: make(chan os.Signal, 1),

		// 无缓冲通道
		complete: make(chan error),

		// time.After(d Duration)表示time.Duration长的时候后返回一条time.Time类型的通道消息
		timeout: time.After(d),
	}
}

// 添加任务
func (r *Runner) Add(tasks ...func(int)) {
	r.tasks = append(r.tasks, tasks...)
}

// 执行所有任务，并监视通道事件
func (r *Runner) Start() error {
	// 注册要接收的信号
	signal.Notify(r.interrupt, os.Interrupt)

	go func() {
		r.complete <- r.run()
	}()

	select {
	case err := <-r.complete:
		return err
	case <-r.timeout: // 超时控制，在指定的time.Duration长的时候后返回一条time.Time类型的通道消息
		return ErrTimeout
	}
}

// 迭代执行每一个已注册的任务
func (r *Runner) run() error {
	for id, task := range r.tasks {
		// 若检测到操作系统发出的中断信号，则返回错误
		if r.gotInterrupt() {
			return ErrInterrupt
		}

		// 没有中断信号则继续执行任务
		task(id)
	}
	return nil
}

// 验证是否接收到了中断信号
func (r *Runner) gotInterrupt() bool {
	select {
	// 当中断事件被触发时发出的信号
	case <-r.interrupt:
		// 停止接收后续的任何信号
		signal.Stop(r.interrupt)
		return true

		// 继续正常运行
	default:
		return false
	}
}
