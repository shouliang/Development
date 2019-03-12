// 初始化变量
package main

import "fmt"

// 变量定义可以包含初始值，每个变量对应一个
var i, j int = 1, 2

func main() {
	var c, python, java = true, false, "no!"
	fmt.Println(i, j, c, python, java)
}
