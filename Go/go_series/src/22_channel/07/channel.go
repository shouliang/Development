// 使用for range变量通道
package main

import "fmt"

func producer(chnl chan int) {
	for i := 0; i < 10; i++ {
		chnl <- i
	}
	close(chnl)
}

func main() {
	ch := make(chan int)

	go producer(ch)

	// for range 循环从通道 ch 接收数据，直到该通道关闭。一旦关闭了 ch，循环会自动结束。
	// 当然从通道读取数据时，若通道为空则阻塞等待
	for v := range ch {
		fmt.Println("Received", v)
	}

}
