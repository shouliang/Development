// 演示并行计算一个数各位的平方和立方，然后阻塞等待最终的结果
package main

import "fmt"

// 计算一个数各位的平方和
func calcSquare(number int, squareop chan int) {
	sum := 0
	for number != 0 {
		digit := number % 10
		sum += digit * digit
		number /= 10
	}
	squareop <- sum
}

// 计算一个数各位的立方和
func calcCubes(number int, cubeop chan int) {
	sum := 0
	for number != 0 {
		digit := number % 10
		sum += digit * digit * digit
		number /= 10
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
