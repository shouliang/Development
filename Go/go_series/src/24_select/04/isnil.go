// 如果 select 只含有值为 nil 的信道，也同样会执行默认情况。
package main

import "fmt"

func main() {
	var ch chan string
	select {
	case v := <-ch:
		fmt.Println("received value", v)
	default:
		fmt.Println("default case executed")
	}
}
