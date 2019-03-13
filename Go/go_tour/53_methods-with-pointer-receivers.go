// 接收者为指针的方法
// 使用接收者为指针类型后，1：避免在每个方法调用中拷贝值 2.方法可以修改接收者指向的值
// 接收者为非指针类型，方法看的是副本，并且无法修改原始值
package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

// 接收者为 *Vertex指针类型
func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := &Vertex{3, 4}
	v.Scale(5)
	fmt.Println(v, v.Abs())
}
