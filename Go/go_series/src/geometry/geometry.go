package main

import (
	"fmt"
	"geometry/rectangle" // 导入自定义包
)

func main() {
	var rectLen, rectWidth float64 = 6, 7
	fmt.Println("Geometrical shape properties")

	area := rectangle.Area(rectLen, rectWidth)
	fmt.Printf("area of rectangle %.2f\n", area)

	diagonal := rectangle.Diagonal(rectLen, rectWidth)
	fmt.Printf("diagonal of rectangle %.2f\n", diagonal)
}
