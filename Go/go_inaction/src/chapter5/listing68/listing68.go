// 展示如何访问另一个包的未公开的标识符的值
package main

import (
	"chapter5/listing68/counters"
	"fmt"
)

func main() {
	// 使用公开的New函数类创建一个未公开的变量
	counter := counters.New(10)

	fmt.Printf("Counter: %d\n", counter)
}
