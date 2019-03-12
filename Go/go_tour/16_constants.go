// 常量
// 常量使用const 关键字
// 常量可以是字符、字符串、bool和数值类型
// 常量不能使用 :=语法定义
package main

import "fmt"

const Pi = 3.14

func main() {
	const World = "world"
	fmt.Println("Hello", World)
	fmt.Println("Happy", Pi, "Day")

	const Truth = true
	fmt.Println("Go rules?", Truth)
}
