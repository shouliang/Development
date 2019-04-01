package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func printer(ch chan int) {
	for i := range ch {
		fmt.Printf("Received %d\n", i)
	}

	wg.Done()
}

// 三部曲：wg.Add() wg.Done() wg.Wait()
// wg.Add(3)-> go f1(){do something wg.Done()}、go f2()、go f3() ->  wg.Wait()
func main() {
	c := make(chan int)

	wg.Add(1)
	go printer(c)

	for i := 1; i <= 10; i++ {
		c <- i
	}
	close(c)

	wg.Wait()
}
