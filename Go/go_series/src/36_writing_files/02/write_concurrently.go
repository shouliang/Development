/*并发写文件
当多个 goroutines 同时（并发）写文件时，我们会遇到竞争条件(race condition)。
因此，当发生同步写的时候需要一个 channel 作为一致写入的条件。

我们将写一个程序，该程序创建 100 个 goroutinues。
每个 goroutinue 将并发产生一个随机数，届时将有 100 个随机数产生。
这些随机数将被写入到文件里面。我们将用下面的方法解决这个问题 .

1.创建一个 channel 用来读和写这个随机数。
2.创建 100 个生产者 goroutine。每个 goroutine 将产生随机数并将随机数写入到 channel 里。
3.创建一个消费者 goroutine 用来从 channel 读取随机数并将它写入文件。这样的话我们就只有一个 goroutinue 向文件中写数据，从而避免竞争条件。
4.一旦完成则关闭文件。
*/
package main

import (
	"fmt"
	"math/rand"
	"os"
	"sync"
)

// 产生随机数并且将 data 写入到 channel 中，
// 之后通过调用 waitGroup 的 Done 方法来通知任务已经完成
func produce(data chan int, wg *sync.WaitGroup) {
	n := rand.Intn(999)
	data <- n
	wg.Done()
}

func consume(data chan int, done chan bool) {
	f, err := os.Create("concurrent")
	if err != nil {
		fmt.Println(err)
		return
	}

	// 从 channel 中读取随机数并且写到文件中
	for d := range data {
		_, err = fmt.Fprintln(f, d)
		if err != nil {
			fmt.Println(err)
			f.Close()
			done <- false
			return
		}
	}
	err = f.Close()
	if err != nil {
		fmt.Println(err)
		done <- false
		return
	}

	// 一旦读取完成并且将随机数写入文件后，
	// 通过往 done 这个 channel 中写入 true 来通知任务已完成。
	done <- true
}

func main() {
	data := make(chan int)
	done := make(chan bool)
	wg := sync.WaitGroup{}

	// 开启100个goroutine produce数据到channel
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go produce(data, &wg)
	}

	go consume(data, done)

	go func() {
		// 等待写入的channel的所有goroutine结束，而后关闭channel
		wg.Wait()
		close(data)
	}()

	// 主进程阻塞等待写入文件完成
	d := <-done
	if d == true {
		fmt.Println("File written successfully")
	} else {
		fmt.Println("File writing failed")
	}
}
