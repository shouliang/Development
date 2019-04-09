// 死锁
// 没有 Go 协程向该信道写入数据，因此 select 语句会一直阻塞，导致死锁。
// 该程序会触发运行时 panic
package main

func main() {
	ch := make(chan string)
	select {
	case <-ch:
		// default:
		// 	fmt.Println("default case executed")
	}
}
