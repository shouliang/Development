// Spinner displays an animation while computing the 45th Fibonacci number
package main

import (
	"fmt"
	"time"
)

// spinner()指示器和fib()同时执行
func main() {
	go spinner(100 * time.Millisecond)
	const n = 45
	fibN := fib(n)
	fmt.Printf("\rFibonacci(%d) = %d\n", n, fibN)
}

func spinner(delay time.Duration) {
	// for循环一直在执行，但是当主goroutine退出时，它也被强制退出
	for {
		for _, r := range `-\|/` {
			fmt.Printf("\r%c", r)
			time.Sleep(delay)
		}
	}
}

func fib(x int) int {
	if x < 2 {
		return x
	}
	return fib(x-1) + fib(x-2)
}
