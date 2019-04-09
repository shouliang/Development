// 空的select
// 除非有 case 执行，select 语句就会一直阻塞着。
// 在这里，select 语句没有任何 case，因此它会一直阻塞，导致死锁。该程序会触发 panic
package main

func main() {
	select {}
}
