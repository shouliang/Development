// 指针
/*
Go指针不支持指针运算

类型 *T是指向类型T的值的指针，其零值是nil
var p *int
& 符号会生成一个指向其作用对象的指针
i := 42
p = &i
* 符号表示指针指向的底层的值
fmt.Println(*p) // 通过指针p 读取 i
*p = 21         // 通过指针p 设置 i
*/
package main

import "fmt"

func main() {
	i, j := 42, 2701
	p := &i
	fmt.Println(*p) // 通过指针p 读取 i
	*p = 21         // 通过指针p 设置 i
	fmt.Println(i)

	p = &j
	*p = *p / 37
	fmt.Println(j)
}
