// 数值常量
package main

import "fmt"

const (
	Big   = 1 << 100  // 左移100位，左移就是乘以2的n次方
	Small = Big >> 99 // 右移99位，右移就是除以2的n次方
)

func needInt(x int) int { return x*10 + 1 }

func needFloat(x float64) float64 {
	return x * 0.1
}

func main() {
	fmt.Println(needInt(Small))
	// fmt.Println(needInt(Big)) // overflows int

	fmt.Println(needFloat(Small))
	fmt.Println(needFloat(Big))
}
