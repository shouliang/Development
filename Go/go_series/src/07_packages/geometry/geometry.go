package main

import (
	"07_packages/geometry/rectangle" // 导入自定义包
	"fmt"
	// 导入了包，却不在代码中使用它，这在 Go 中是非法的。当这么做时，编译器是会报错的。
	// 其原因是为了避免导入过多未使用的包，从而导致编译时间显著增加
	// 然而，在程序开发的活跃阶段，又常常会先导入包，而暂不使用它。遇到这种情况就可以使用空白标识符 _。
	// _ "07_packages/geometry/rectangle" // _ 空白标识符在此只会调用包中的init函数，而不会使用包中的函数和变量
	"log"
)

// 包级别变量
var rectLen, rectWidth float64 = 6, 7

// 包含一个 init 函数。init 函数不应该有任何返回值类型和参数，
// 在我们的代码中也不能显式地调用它。init 函数的形式如下：
// func init() {
// }
// 如果一个包导入了另一个包，会先初始化被导入的包。
// 尽管一个包可能会被导入多次，但是它只会被初始化一次。

func init() {
	fmt.Println("main package initialized")
	if rectLen < 0 {
		//log.Fatal 函数打印一条日志，并终止了程序。
		log.Fatal("length is less than zero")
	}
	if rectWidth < 0 {
		log.Fatal("width is less than zero")
	}
}

func main() {

	fmt.Println("Geometrical shape properties")

	area := rectangle.Area(rectLen, rectWidth)
	fmt.Printf("area of rectangle %.2f\n", area)

	diagonal := rectangle.Diagonal(rectLen, rectWidth)
	fmt.Printf("diagonal of rectangle %.2f\n", diagonal)
}
