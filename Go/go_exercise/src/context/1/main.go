// WaitGroup控制并发
package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		defer wg.Done()
		time.Sleep(2 * time.Second)
		fmt.Println("first finished")
	}()
	go func() {
		defer wg.Done()
		time.Sleep(2 * time.Second)
		fmt.Println("second finished")
	}()

	wg.Wait()
	fmt.Println("All done")
}
