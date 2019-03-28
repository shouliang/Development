// 展示如何使用基本的log包
package main

import "log"

func init() {
	log.SetPrefix("TRACE: ")
	log.SetFlags(log.Ldate | log.Lmicroseconds | log.Llongfile)
}

func main() {
	// 输出到标准日志记录器
	log.Println("message")

	// 在调用Println() 之后会接着调用os.Exit(1)
	log.Fatalln("fatal message")

	// 在调用Println() 之后会接着调用panic()
	log.Panicln("Panic message")
}
