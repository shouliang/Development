// 结构体指针
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9 // 结构体字段可以通过结构体指针来访问
	fmt.Println(v)
}
