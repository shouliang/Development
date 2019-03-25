// channel的关闭和广播
package channel_close

import (
	"fmt"
	"sync"
	"testing"
)

func dataProducer(ch chan int, wg *sync.WaitGroup) {
	go func() {
		for i := 0; i < 10; i++ {
			ch <- i
		}
		close(ch)
		//向关闭的channel发送数据，会导致panic
		//ch <- 11
		wg.Done()
	}()
}

func dataReceiver(ch chan int, wg *sync.WaitGroup) {
	go func() {
		// 第一版
		// for i := 0; i < 10; i++ {
		// 	data := <-ch
		// 	fmt.Println(data)
		// }

		// 第二版
		// for i := 0; i < 10; i++ {
		// 	if data, ok := <-ch; ok {
		// 		fmt.Println(data)
		// 	}
		// }

		// 第三版
		// 第11个数，接收不到， 会被阻塞,如果channel关闭，就不会阻塞，而是输出通道类型的零值
		// for i := 0; i < 11; i++ {
		// 	fmt.Println(<-ch)
		// }

		// 第四版
		// ok 为true表示通道正常接收，false表示通道关闭
		// 所有channel接收者都会在channel关闭时，立即从阻塞等待中返回且ok返回false。这个广播机制被利用向多个订阅者同时发送信号，如：退出信号
		for {
			if data, ok := <-ch; ok {
				fmt.Println(data)
			} else {
				break
			}
		}

		wg.Done()
	}()
}

func TestCloseChannel(t *testing.T) {
	var wg sync.WaitGroup
	ch := make(chan int)

	wg.Add(1)
	dataProducer(ch, &wg)

	wg.Add(1)
	dataReceiver(ch, &wg)

	wg.Wait()
}
