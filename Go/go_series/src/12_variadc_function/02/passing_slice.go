// 给可变参数函数传入切片
package main

import "fmt"

func find(num int, nums ...int) {
	fmt.Printf("type of nums is %T\n", nums)
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
	nums := []int{90, 89, 95}

	// 试图传入切片类型的参数会类型错误
	// find(89, nums) // cannot use nums (type []int) as type int in argument to find

	// 有一个可以直接将切片传入可变参数函数的语法糖，你可以在在切片后加上 ... 后缀。
	// 如果这样做，切片将直接传入函数，不再创建新的切片
	find(89, nums...)
}
