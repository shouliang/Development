// 数组是值类型而不是引用类型。这意味着当数组赋值给一个新的变量时，
// 该变量会得到一个原始数组的一个副本。如果对新变量进行更改，则不会影响原始数组。
package main

import "fmt"

func main() {
	a := [...]string{"USA", "China", "India", "Germany", "France"}
	b := a
	b[0] = "Singapore"
	fmt.Println("a is", a)
	fmt.Println("b is", b)
}
