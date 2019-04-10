// 通道的声明: make
package main

import "fmt"

func main() {
	var a chan int

	// 通道的零值为nil
	if a == nil {
		fmt.Println("channel a is nil,going to define it")

		// make定义了int类型的通道
		a = make(chan int)
		fmt.Printf("Type of a is %T\n", a)
	}
}
