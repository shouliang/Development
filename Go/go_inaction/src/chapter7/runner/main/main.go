// 展示如何利用通道来检查程序的运行时间
// 以及在程序运行过长时间后如何终止程序
package main

import (
	"chapter7/runner"
	"log"
	"os"
	"time"
)

// timeout规定了必须在多少秒内处理完成
const timeout = 3 * time.Second

func main() {
	log.Println("Starting work.")

	// 分配超时时间
	r := runner.New(timeout)

	// 加入要执行的任务
	r.Add(createTask(), createTask(), createTask())

	// 执行任务并处理返回结果
	if err := r.Start(); err != nil {
		switch err {
		case runner.ErrTimeout:
			log.Println("Terminating due to timeout.")
			os.Exit(1)
		case runner.ErrInterrupt:
			log.Println("Terminating due to interrupt")
			os.Exit(2)

		}
	}

	log.Println("Process ended.")

}

// 创建任务函数，根据id休眠指定秒数
func createTask() func(int) {
	return func(id int) {
		log.Printf("Processor - Task #%d.", id)
		time.Sleep(time.Duration(id) * time.Second)
	}
}
