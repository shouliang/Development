// 命名的函数返回值

package main

import "fmt"

// 从函数中可以返回一个命名值。一旦命名了返回值，可以认为这些值在函数第一行就被声明为变量了。
// 此例中area, perimeter就是被命名的函数返回值
func rectProps(length, width float64) (area, perimeter float64) {
	area = length * width
	perimeter = (length + width) * 2

	// 不需要明确指定返回值，默认返回 area, perimeter 的值
	return
}

func main() {
	area, perimeter := rectProps(10.8, 5.6)
	fmt.Printf("Area %f Preimeter %f\n", area, perimeter)
}
