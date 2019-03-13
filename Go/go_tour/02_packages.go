// 包
// 每个Go程序都是由包组成的
package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("My favorite number is ", rand.Intn(10)) // 按照惯例，包名与导入路径的最后一个目录一致，此处为rand
}
