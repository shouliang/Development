// 包声明，表明代码所在的模块(包)，命令源码文件包名必须是main，文件名不一定是 main.go,此处即为hello_world.go
// 包名也不一定与其所在目录同名，但强烈建议同名
// 命令源码文件和库文件也不要放同一个包中，防止无法执行 go build 和 go install
package main

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
