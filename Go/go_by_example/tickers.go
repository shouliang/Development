// 打点器
package main

import (
	"fmt"
	"time"
)

func main() {
	ticker := time.NewTicker(time.Millisecond * 500)

	go func() {
		// 我们在这个通道上使用内置的 range 来迭代值每隔500ms 发送一次的值。
		for t := range ticker.C {
			fmt.Println("Tick at", t)
		}
	}()

	//我们将在运行后 1600ms停止这个打点器。
	time.Sleep(time.Millisecond * 1600)
	ticker.Stop()
	fmt.Println("Ticker stopped")
}
