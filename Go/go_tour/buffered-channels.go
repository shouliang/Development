// 缓冲 channel
/*
channel 可以是 带缓冲的，为make提供第二个参数作为缓冲长度来初始化一个缓冲 channel
ch := make(chan int, 100)
向缓冲channel 发送数据的时候，只有在缓存区满的时候才会阻塞，当缓冲区清空的时候接受阻塞
*/
package main

import "fmt"

func main() {
	c := make(chan int, 2)
	c <- 1
	c <- 2
	//c <- 3    // channel已满，不能再发送数据到channel
	fmt.Println(<-c)
	fmt.Println(<-c)
	c <- 998
	c <- 999
	fmt.Println(<-c)
	fmt.Println(<-c)
	//fmt.Println(<-c) channel已空，不能再从channel读取数据
}
