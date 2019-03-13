// 接口
// 接口类型是由一组方法定义的集合
// 接口类型的值可以存放实现这些方法的任何值
package main

import (
	"fmt"
	"math"
)

// 定义接口
type Abser interface {
	Abs() float64
}

type MyFloat float64

// 数据类型MyFloat实现了接口中的Abs()方法
func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}

	return float64(f)
}

type Vertex struct {
	X, Y float64
}

// 数据类型 *Vertex实现了接口中的Abs()方法
func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	var a Abser // 声明一个接口变量，可以存放实现接口的任意值
	f := MyFloat(-math.Sqrt2)
	v := Vertex{3, 4}

	a = f // a MyFloat实现了接口 Abser
	fmt.Println(a.Abs())

	a = &v // a *Vertex 实现了接口 Abser
	fmt.Println(a.Abs())

	// a = v // a Vertex 没有实现了接口 Abser，故此句会编译不通过
}
