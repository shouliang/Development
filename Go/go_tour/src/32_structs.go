// 结构体
// 一个结构体struct就是一个字段的集合
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	fmt.Println(Vertex{1, 2})
}
