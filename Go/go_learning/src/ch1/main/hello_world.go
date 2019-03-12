// 包声明，表明代码所在的模块(包)，命令源码文件包名必须是main，文件名不一定是 main.go,此处即为hello_world.go
// 包名也不一定与其所在目录同名，但强烈建议同名
// 命令源码文件和库文件也不要放同一个包中，防止无法执行 go build 和 go install,除非库文件的包声明也是main
package main

// 引入代码依赖
// 同一个包下可以有多个库文件，每个库文件的包声明都相同
import (
	"ch1/lib_my" // 注意引入的是路径，是相对于当前工作区的src目录的路径，故都是目录名，然而引用包成员时使用包名而非目录名，所以建议目录名和包名一致
	"fmt"
	"os"
)

// 功能实现，必须是main方法
// main 函数不支持任何返回值，可通过 os.Exit来返回状态
// main 函数不支持传入参数，可通过 os.Args获取命令行参数
func main() {
	if len(os.Args) > 1 {
		fmt.Println("os.Args is", os.Args)
		fmt.Println("Hello World", os.Args[1])
	} else {
		fmt.Println("Hello World No Args")
	}

	// 引用外部代码包的方式：在同一个代码包，不在同一个代码包

	// 同属于main包，可以直接引用lib1.go中的hellofromlib1()方法
	// 1.通过go run hello_world.go lib1.go 来运行
	// 2.或者先编译 go build 而后再运行生成的可执行程序
	// fmt.Println(hellofromlib1())

	// 首字母大写
	fmt.Println(lib.HelloFromLib2())

	//fmt.Println(lib.helloFromLib2())

	// 引用方法前有限定符lib,即为程序实体的包名，而非目录名
	fmt.Println(lib.HelloFromLib3())

	os.Exit(0)
}
