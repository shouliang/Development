package main

import "fmt"

func main() {
	// make创建 len 和 cap 均为5的切片
	slice1 := make([]string, 5)
	fmt.Println("slice1", slice1, len(slice1), cap(slice1))

	// make创建 len=3 和 cap=5 的切片
	slice2 := make([]int, 3, 5)
	fmt.Println("slice2", slice2, len(slice2), cap(slice2))

	// 字面量来声明切片
	slice3 := []string{"Red", "Blue", "Green", "Yellow", "Pink"}
	fmt.Println("slice3", slice3, len(slice3), cap(slice3))

	// 使用索引声明切片  中括号[]里面有数字是数组类型，无数字是切片类型
	slice4 := []string{99: "hello"}
	fmt.Println("slice4", len(slice4), cap(slice4))

	// 使用切片创建切片，共享同一段底层数组
	// 对于底层数组容量为c的切片slice[i:j]来说，len = j - i; cap =c -i，索引从i到j-1
	slice5 := []int{10, 20, 30, 40, 50}
	slice6 := slice5[1:3]
	fmt.Println("slice5", slice5, len(slice5), cap(slice5))
	fmt.Println("slice6", slice6, len(slice6), cap(slice6))

	// 一个切片修改了底层数组，另一个切片也能感知到
	slice6[1] = 36
	fmt.Println("after slice6[1] = 36 slice5 ", slice5)
	fmt.Println("after slice6[1] = 36 slice 6", slice6)

	// 修改不存在的元素，会产生越界错误,slice6的len=2，只能修改索引为0，1的元素
	// slice6[2] = 55 //panic: runtime error: index out of range

	// append后会返回一个包含修改结果的新切片
	//              若原切片还有容量：继续共享原切片的底层数组，故修改后原切片的底层数组中的元素也会被修改
	//              若超过原切片容量：创建一个新的底层数组，将现有的值复制到新数组里，再追加新的值
	slice7 := append(slice6, 60)
	fmt.Println("slice6", slice6)
	fmt.Println("slice7", slice7)
	// slice5索引3的值40被替换成60个
	fmt.Println("slice5", slice5)

	// append后超过原始切片的容量会创建一个新的底层数组，将现有值赋值到新数组，再追加值
	slice8 := []int{10, 20, 30, 40}
	slice9 := append(slice8, 50)
	fmt.Println("slice8", slice8)
	fmt.Println("slice9", slice9)

	// range创建了每个元素的副本，而不是直接返回对该元素的引用  TODO:待理解
	slice10 := []int{10, 20, 30, 40}
	fmt.Println("slice10 Address ", &slice10)
	for index, value := range slice10 {
		fmt.Println(value, &value, &slice10[index]) // 此处&value均相同
	}

	// 迭代切片 for range
	for index, value := range slice8 {
		fmt.Println(index, value)
	}
	//也可以使用空白标识符_来忽略索引值
	for _, value := range slice8 {
		fmt.Println(value)
	}

	// 也可以选择传统的for循环
	for index := 2; index < len(slice8); index++ {
		fmt.Println("Index:", index, "Value:", slice8[index])
	}

	// 多维切片
	sliceMulti := [][]int{{10}, {100, 200}}
	fmt.Println(sliceMulti)

	sliceMulti[0] = append(sliceMulti[0], 20)
	fmt.Println(sliceMulti)

	// 在函数间传递切片
	slice := make([]int, 1e6)
	slice = foo(slice)

}

// 由于切片关联的数据包含在底层数组里，而不属于切片本身
// 所以切片复制到任意函数时，对底层数组大小都不会有影响
// 复制时只会复制切片本身
// 64位架构机器上，一个切片24字节内存：指针字段、长度和容量都是8字节
func foo(slice []int) []int {
	return slice
}
