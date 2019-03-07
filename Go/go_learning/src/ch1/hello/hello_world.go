package main // 包，表明代码所在的模块(包)，必须是main包，文件名不一定是 main.go
// package main1

// 引入代码依赖
import (
	"fmt"
	"os"
)

// 功能实现，必须是main方法
// main 函数不支持任何返回值，可通过 os.Exit来返回状态
// main 函数不支持传入参数，可通过 os.Args获取命令行参数
func main() {
	if len(os.Args) > 1 {
		fmt.Println("Hello World", os.Args[1])
	}
	fmt.Println("Hello World")
	os.Exit(0)
}
