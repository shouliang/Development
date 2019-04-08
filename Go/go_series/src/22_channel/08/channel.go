// 演示并行计算一个数各位的平方和立方，然后阻塞等待最终的结果
package main

import "fmt"

// 将一个数的各位发送到一个通道里面
func digits(number int, dchnl chan int) {
	for number != 0 {
		digit := number % 10
		dchnl <- digit
		number /= 10
	}
	close(dchnl)
}

// 计算一个数各位的平方和
func calcSquare(number int, squareop chan int) {
	sum := 0
	dch := make(chan int)

	// 并发调用digits
	go digits(number, dch)

	for digit := range dch {
		sum += digit * digit
	}

	squareop <- sum
}

// 计算一个数各位的立方和
func calcCubes(number int, cubeop chan int) {
	sum := 0
	dch := make(chan int)

	// 并发调用digits
	go digits(number, dch)

	for digit := range dch {
		sum += digit * digit * digit
	}

	cubeop <- sum
}

func main() {
	number := 123
	square := make(chan int)
	cube := make(chan int)

	// 开启2个协程，并发计算
	go calcSquare(number, square)
	go calcCubes(number, cube)

	// 在此处阻塞等待，直到squares, cubes两个通道有值
	squares, cubes := <-square, <-cube
	fmt.Printf("%d + %d = %d\n", squares, cubes, squares+cubes)
}
