// 演示结构体嵌套和匿名成员
package main

import "fmt"

type Point struct {
	X, Y int
}

type Circle struct {
	Point  // 匿名成员
	Radius int
}

type Wheel struct {
	Circle // 匿名成员
	Spokes int
}

func main() {
	var w Wheel
	w = Wheel{
		Circle: Circle{
			Point:  Point{X: 8, Y: 8},
			Radius: 5,
		},
		Spokes: 20,
	}
	fmt.Printf("%#v\n", w)
}
