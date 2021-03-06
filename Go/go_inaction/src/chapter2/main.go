// main函数必须包含在名为main的包中
package main

import (
	_ "chapter2/matchers"
	"chapter2/search" //引入search包，会先执行search包中所有文件的init方法
	"log"
	"os"
)

// init 在main之前调用
func init() {
	// 将日志输出到标准输出
	log.SetOutput(os.Stdout)
}

// main 是整个程序的入口
func main() {
	// 一旦Run函数退出，程序就会终止
	search.Run("president")
}
