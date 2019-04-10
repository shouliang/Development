/*
我们工作池的核心功能如下：
创建一个 Go 协程池，监听一个等待作业分配的输入型缓冲通道。
将作业添加到该输入型缓冲通道中。
作业完成后，再将结果写入一个输出型缓冲通道。
从输出型缓冲通道读取并打印结果。
*/

/*
可以想象成 多个worker协程处理jobs通道中的job，只要通道不为空即可，为空则阻塞等待；
此时也可进行分配工作到通道jobs，只要通道不满即可，满则阻塞

有缓存的通道： 可以在同时向有缓存的通道中写数据(只要通道未满，否则阻塞写)和读数据(只要通道未空，否则阻塞读)
另注意：发送者主动close通道，否则通道为空时读取时会报错
*/

package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

// 定义工作结构体
type Job struct {
	id       int
	randomno int
}

// 定义处理工作完的结果 结构体
type Result struct {
	job         Job
	sumofdigits int
}

// 初始化工作通道大小为10
var jobs = make(chan Job, 10)

// 初始化处理后的结果的通道大小也为10
var results = make(chan Result, 10)

// 计算各位数之和
func digits(number int) int {
	sum := 0
	no := number
	for no != 0 {
		digit := no % 10
		sum += digit
		no /= 10
	}

	// 模拟处理时间为2秒
	time.Sleep(time.Second * 2)
	return sum
}

// 分配工作到jobs通道
// 若通道未满：可继续分配工作
// 若通道已满：被阻塞住，等待被处理
//                            若被处理后，则通道未满，可继续分配工作，直到所有的工作分配完毕，故job数量可以远远大于通道容量
func allocate(noOfJobs int) {
	for i := 0; i < noOfJobs; i++ {
		jobs <- Job{i, rand.Intn(999)}
	}

	// 分配完所有job,关闭jobs通道
	// 通道由发送者关闭
	close(jobs)
}

// 处理工作通道jobs中的job
// 若jobs通道为空：则阻塞住，等待分配工作
// 若jobs通道为不为空：则处理分配的工作将结果保存到结果通道results中
func worker(wg *sync.WaitGroup) {
	for job := range jobs {
		results <- Result{job, digits(job.randomno)}
	}

	// 若jobs通道关闭，则通知主进程该worker已经完成
	wg.Done()
}

// 工作池: 初始化多个worker协程处理工作
func createWorkerPool(noOfWorkers int) {
	var wg sync.WaitGroup

	// 初始化多个worker协程同时工作
	for i := 0; i < noOfWorkers; i++ {
		wg.Add(1)
		go worker(&wg)
	}

	// 等待所有工作处理完毕
	wg.Wait()

	// 所有工作处理完毕后，关闭处理结果的通道results
	// 通道由发送者关闭
	close(results)
}

// 打印处理结果通道results中的信息
// 若通道results不为空：则可打印
// 若通道results为空：则阻塞
// 若通道results关闭，则结束，通过done通知主进程
func result(done chan bool) {
	for result := range results {
		fmt.Printf("Job id %d, input random no %d, sum of digits %d\n", result.job.id, result.job.randomno, result.sumofdigits)
	}

	done <- true
}

// 分配工作 allocate 和  处理工作 worker 和 打印结果result 可以同时进行
func main() {
	statrTime := time.Now()

	noOfJobs := 100
	go allocate(noOfJobs)

	// 等待结果的打印操作结束的同步标志
	done := make(chan bool)
	go result(done)

	noOfWorkers := 10
	createWorkerPool(noOfWorkers)

	// 主进程在此处阻塞，直到结果的打印操作完成后解除
	<-done

	endTime := time.Now()
	diff := endTime.Sub(statrTime)
	fmt.Println("total time taken", diff.Seconds(), "seconds")
}
