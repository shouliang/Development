// for（续）
// 前置; ;后置
// 前置和后置语句可以为空
package main

import "fmt"

func main() {
	sum := 1
	// for ; sum < 1000 ; {
	// sum += sum
	//}
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)
}
