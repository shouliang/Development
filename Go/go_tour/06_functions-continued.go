// 函数(续)
package main

import "fmt"

// 当两个或多个连续的函数命名参数是同一类型，则除了最后一个类型之外，其他都可以省略
// 此例中 x int, y int 被缩写为 x, y int
func add(x, y int) int {
	return x + y
}

func main() {
	fmt.Println(add(42, 13))
}
