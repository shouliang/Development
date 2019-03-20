package main

import "fmt"

func main() {
	// 声明一个包含5个元素的整型数组
	// 一旦声明，数组里的数据类型和数组长度就都不能改变了
	// 每个元素都初始化为对应类型的零值
	var array1 [5]int
	fmt.Println(array1)

	// 初始化
	array2 := [5]int{10, 20, 30, 40, 50}
	fmt.Println(array2)

	// ... 容量由初始化值的数量决定
	array3 := [...]int{10, 20, 30, 40, 50, 60}
	fmt.Println(len(array3))

	// 修改数组里面的元素
	array3[2] = 35
	fmt.Println(array3)

	// 声明包含5个元素的指向整数的数组
	// 用整型指针初始化索引为0和1的数组元素
	array4 := [5]*int{0: new(int), 1: new(int)}
	fmt.Println(array4)
	// 为索引0和1的元素赋值
	*array4[0] = 11
	*array4[1] = 22
	fmt.Println(*array4[0])

	// 同样类型的一个数组赋值给另外一个数组，复制之后两个数组的值完全一样
	array5 := [5]string{"Red", "Blue", "Green", "Yellow", "Pink"}
	array6 := array5
	array6[0] = "BigRed" // 改变array6的数组，并不会影响到array5,因为它只是array5的一个副本
	fmt.Println(array5)
	fmt.Println(array6)

	// 数组变量的类型包括数组长度和每个元素的类型，只有这两部分都相同的数组，才是类型相同的数组，才能互相赋值
	// var array7 [4]string
	// array7 = [5]string{"Red", "Blue", "Green", "Yellow", "Pink"} // cannot use [5]string literal (type [5]string) as type [4]string in assignment

	// 声明字符串指针类型的数组
	var array8 [3]*string
	array9 := [3]*string{new(string), new(string), new(string)}
	// 复制后，两个数组指向同一组字符串
	array8 = array9
	fmt.Println(array8 == array9)
	*array8[0] = "Red" //改变array8中的元素，相当于改变array9中的元素
	fmt.Println(*array9[0])

	// 声明一个二维整型数组
	var array10 [4][2]int
	array10 = [4][2]int{{10, 11}, {20, 21}, {30, 32}, {40, 41}}
	fmt.Println(array10)

	// 声明一个需要8MB的数组
	var array11 [1e6]int

	// func foo(array [1e6]int){
	//
	// }
	foo(&array11)
}

// 在函数间传递变量时总是以值的方式传递的
// 这就意味着传递一个变量时数组时，不管多长，都会完整复制并传递给函数
// 建议采取只传入指向数组的指针

// 不建议：传递数组值，会复制一份副本
// func foo(array [1e6]int) {
// 	fmt.Println(len(array))
// }

// 建议：传递数组指针，如果改变指针指向的值，会改变共享的内存
func foo(array *[1e6]int) {
	fmt.Println(len(array))
}
