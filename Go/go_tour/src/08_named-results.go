// 命名返回值
package main

import "fmt"

// x,y 就是命名的返回值 return语句返回结果的当前值
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func main() {
	fmt.Println(split(17))
}
