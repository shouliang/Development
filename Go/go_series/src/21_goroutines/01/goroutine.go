// 如何启动一个Go协程
// 调用函数或者方法时，在前面加上关键字 go，可以让一个新的 Go 协程并发地运行。
package main

import (
	"fmt"
	"time"
)

func hello() {
	fmt.Println("Hello world goroutine")
}

// go hello() 启动了一个新的 Go 协程。协程的调用会立即返回。
// 现在 hello() 函数与 main() 主函数会并发地执行
// 主函数会运行在一个特有的 Go 协程上，它称为 Go 主协程（Main Goroutine）
// Go 主协程终止，则程序终止，于是其他 Go 协程也不会继续运行。
func main() {
	go hello()
	fmt.Println("main function")

	// 主进程等待1秒后结束
	time.Sleep(1 * time.Second)
}
