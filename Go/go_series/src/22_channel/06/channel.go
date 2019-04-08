// 关闭通道和使用for range变量通道
package main

import "fmt"

func producer(chnl chan int) {
	for i := 0; i < 10; i++ {
		chnl <- i
	}

	// 发送方可以关闭通道，通知接收方这个信道不再有数据发送过来
	close(chnl)
}

func main() {
	ch := make(chan int)

	go producer(ch)

	// 无限循环
	for {
		// 从通道接收数据，并检测通道是否已经关闭，关闭则break
		v, ok := <-ch
		if ok == false {
			break
		}
		fmt.Println("Received", v, ok)
	}

}
