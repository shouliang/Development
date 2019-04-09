// 空白符
// _ 在 Go 中被用作空白符，可以用作表示任何类型的任何值。
package main

import "fmt"

func rectProps(length, width float64) (float64, float64) {
	var area = length * width
	var perimeter = (length + width) * 2
	return area, perimeter
}

func main() {
	// 只使用area,返回的perimeter被舍弃
	area, _ := rectProps(10.8, 5.6)
	fmt.Printf("Area %f \n", area)
}
