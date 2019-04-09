// 数组的大小是类型的一部分。因此 [3]int 和 [5]int 是不同类型
package main

func main() {
	a := [3]int{5, 9, 4}
	var b [5]int
	b = a //cannot  use a (type [3]int) as type [5]int in assignment
}
