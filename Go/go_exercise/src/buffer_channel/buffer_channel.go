// 演示向有缓存的通道分配job(只要通道未满即可)，可同时处理通道里面的job(只要通道未空即可)
package main

import "fmt"

var jobsChannel = make(chan int, 10)

// 分配工作(allocateJobs)和处理工作(handleJobs)，可以同时进行
func main() {
	noOfJobs := 30
	go allocateJobs(noOfJobs)

	done := make(chan bool)
	go handleJobs(done)

	// 等待工作处理完成
	<-done
}

// 分配工作
func allocateJobs(noOfJos int) {
	for i := 0; i < noOfJos; i++ {
		fmt.Println("allocating job", i)
		jobsChannel <- i
	}

	// 分配完所有工作，关闭通道，不关闭的话：for range遍历到通道为空的时候会报错
	close(jobsChannel)
}

// 处理工作
func handleJobs(done chan bool) {
	for i := range jobsChannel {
		fmt.Println("handling job", i)
	}

	// 通知主进程，所有工作已处理完毕
	done <- true
}
