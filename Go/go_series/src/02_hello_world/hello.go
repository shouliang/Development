package main

import "fmt"

// go build 默认会创建所在目录同名的可执行程序
// go install会在当前工作区的bin目录下安装可执行程序
func main() {
	fmt.Println("Hello World")
}
