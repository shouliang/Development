// 展示公开的结构类型中如何访问未公开的内嵌类型
package main

import (
	"chapter5/listing74/entities"
	"fmt"
)

func main() {
	a := entities.Admin{
		Rights: 10,
	}

	// 可以设置未公开的内部类型的 公开字段
	a.Name = "Bill"
	a.Email = "bill@gmail.com"

	fmt.Printf("User: %v\n", a)
}
