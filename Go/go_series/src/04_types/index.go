// int：根据不同的底层平台（Underlying Platform），表示 32 或 64 位整型。
// 除非对整型的大小有特定的需求，否则你通常应该使用 int 表示整型。
// int类型大小：在 32 位系统下是 32 位，而在 64 位系统下是 64 位。
package main

import (
	"fmt"
	"unsafe"
)

func main() {
	var a int = 89
	b := 95
	fmt.Println("value of a is", a, "and b is", b)
	fmt.Printf("type of a is %T, size of a is %d\n", a, unsafe.Sizeof(a)) // a 的类型和大小
	fmt.Printf("type of b is %T, size of b is %d\n", b, unsafe.Sizeof(b)) // b 的类型和大小
}
