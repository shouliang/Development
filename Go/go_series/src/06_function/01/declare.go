/* 函数的声明和调用

func functionname(parametername type) returntype {
    // 函数体（具体实现的功能）
}

*/
package main

import "fmt"

// 如果有连续若干个参数，它们的类型一致，那么我们无须一一罗列，
// 只需在最后一个参数后添加该类型
func calculateBill(price, no int) int {
	var totalPrice = price * no
	return totalPrice
}

func main() {
	price, no := 90, 6

	// 调用函数的语法为 functionname(parameters)
	totalPrice := calculateBill(price, no)
	fmt.Println("Total price is", totalPrice)
}
