// 结构体文法
// 结构体文法表示通过结构体字段的值作为列表来新分配一个结构体
// 使用 Name: 语法可以仅列出部分字段
package main

import (
	"fmt"
)

type Vertex struct {
	X, Y int
}

var (
	v1 = Vertex{1, 2}  // 类型为Vertex
	v2 = Vertex{X: 1}  // Y:0 被省略
	v3 = Vertex{}      // X:0 和 Y:0
	p  = &Vertex{1, 2} // &前缀返回一个结构体的指针类型 *Vertex
)

func main() {
	fmt.Println(v1, v2, v3, p)
}
