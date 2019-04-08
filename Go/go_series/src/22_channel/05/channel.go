// 单向通道
package main

// 唯送通道，只可以向通道发送数据
func sendData(sendch chan<- int) {
	sendch <- 10
}

func main() {
	sendch := make(chan<- int)
	go sendData(sendch)
	//fmt.Println(<-sendch) // <-sendch (receive from send-only type chan<- int)
}
