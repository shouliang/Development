// 类型推导
// 在定义一个变量但不指定其类型时，变量的类型由右值推导得出
package main

import "fmt"

func main() {
	// v := 42
	v := "a string"
	fmt.Printf("v is of type %T\n", v) // %T输出数据类型

	i := 42
	f := 3.1415
	fmt.Printf("%[1]d is of type %[1]T\n", i)
	fmt.Printf("%[1]f is of type %[1]T\n", f)

}
