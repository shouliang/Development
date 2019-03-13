package main

import "fmt"

func fibonacci() func() int {
	first, second, fibsum := 0, 1, 0

	return func() int {
		fibsum = frist + second
		first, second = second, fibsum
		return fibsum
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
