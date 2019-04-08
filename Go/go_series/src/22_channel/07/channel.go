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

	// for range 循环从信道 ch 接收数据，直到该信道关闭。一旦关闭了 ch，循环会自动结束。
	for v := range ch {
		fmt.Println("Received", v)
	}

}
