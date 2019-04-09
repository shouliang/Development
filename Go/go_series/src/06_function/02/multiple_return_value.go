// 函数可以有多返回值
package main

import "fmt"

// 如果一个函数有多个返回值，那么这些返回值必须用 ( 和 ) 括起来
func rectProps(length, width float64) (float64, float64) {
	var area = length * width
	var perimeter = (length + width) * 2
	return area, perimeter
}

func main() {
	area, perimeter := rectProps(10.8, 5.6)
	fmt.Printf("Area %f Preimeter %f\n", area, perimeter)
}
