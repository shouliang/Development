// 死锁
package main

import "fmt"

func main() {
	ch := make(chan string, 2)
	ch <- "naveen"
	ch <- "paul"

	// 超出了通道的容量(2)，因此这次写入发生了阻塞。
	// 现在想要这次写操作能够进行下去，必须要有其它协程来读取这个通道的数据。
	// 但在本例中，并没有并发协程来读取这个通道，因此这里会发生死锁（deadlock）。
	ch <- "steve"
	fmt.Println(<-ch)
	fmt.Println(<-ch)
}
