// 这个指南构建在 Go Playground 之上，这是一个运行在 golang.org 的服务器上的一个 Web 服务。
// 服务接收 Go 程序的输入，且在沙盒里编译、链接和运行， 然后返回输出。
package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Welcome to the playground")

	fmt.Println("The time is", time.Now())
}
