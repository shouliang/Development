// 可变参数
// 可变参数函数的工作原理是把可变参数转换为一个新的切片
// 如果函数最后一个参数被记作 ...T ，这时函数可以接受任意个 T 类型参数作为最后一个参数。
package main

import "fmt"

func find(num int, nums ...int) {
	fmt.Printf("type of nums is %T\n", nums) // nums是[]int切片类型
	found := false
	for i, v := range nums {
		if v == num {
			fmt.Println(num, "found at index", i, "in", nums)
			found = true
		}
	}

	if !found {
		fmt.Println(num, "not found in", nums)
	}
	fmt.Printf("\n")
}

func main() {
	find(89, 90, 89, 95)
	find(45, 56, 67, 45, 90, 109)
	find(78, 38, 56, 98)

	// 不给可变参数传入参数也是合法的，此时可变参数是一个长度和容量均为0的nil切片
	find(87)
}
