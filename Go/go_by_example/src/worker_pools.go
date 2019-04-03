// 工作池
package main

import (
	"fmt"
	"time"
)

func worker(id int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		fmt.Println("worker", id, "processing job", j)

		// 模拟耗时的任务
		time.Sleep(time.Second)

		// 通知主进程该次任务已经完成
		results <- j * 2
	}
}

func main() {
	jobs := make(chan int, 100)
	results := make(chan int, 100)

	// 3个worker 并发执行9个job
	for w := 1; w <= 3; w++ {
		go worker(w, jobs, results)
	}

	//  9个job
	for j := 1; j <= 9; j++ {
		jobs <- j
	}
	close(jobs)

	for a := 1; a <= 9; a++ {
		// 阻塞在此等待任务完成
		<-results
	}
}
