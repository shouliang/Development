// 展示不能总是获取值的地址
package main

import "fmt"

// duration 是一个基于int类型的类型
type duration int

func (d *duration) pretty() string {
	return fmt.Sprintf("Duration: %d", *d)
}

func main() {
	duration(42).pretty()
	// cannot call pointer method on duration(42)
	// cannot take the address of duration(42)
}
