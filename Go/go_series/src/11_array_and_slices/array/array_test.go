package arraytest

import (
	"fmt"
	"testing"
)

// 数组是同一类型元素的集合。例如，整数集合 5,8,9,79,76 形成一个数组。
// Go 语言中不允许混合不同类型的元素，例如包含字符串和整数的数组。
// （译者注：当然，如果是 interface{} 类型数组，可以包含任意类型）

// 数组的声明
// 一个数组的表示形式为 [n]T。n 表示数组中元素的数量，T 代表每个元素的类型。
// 元素的数量 n 也是该类型的一部分
func TestDeclareArray(t *testing.T) {
	// var a[3]int 声明了一个长度为 3 的整型数组。数组中的所有元素都被自动赋值为数组类型的零值。
	var a [3]int
	t.Log(a)

	// 声明而后赋值
	var b [3]int
	b[0] = 1
	b[1] = 2
	b[2] = 3
	t.Log(b)

	// 声明并初始化
	var c = [3]int{4, 5, 6}
	t.Log(c)

	// 简略声明
	d := [3]int{7, 8, 9}
	t.Log(d)

	// 在简略声明中，不需要将数组中所有的元素赋值。
	e := [6]int{10, 11, 12}
	t.Log(e)

	// 你甚至可以忽略声明数组的长度，并用 ... 代替，让编译器为你自动计算长度
	f := [...]int{13, 14, 15, 16, 17, 18}
	t.Log("f is", f, "and lenght is", len(f)) // len获取数组长度

	// 数组的大小是类型的一部分。因此 [5]int 和 [25]int 是不同类型
	// g := [3]int{5, 9, 4}
	// var h [5]int
	// h = g //cannot use g (type [3]int) as type [5]int in assignment
}

// 数组是值类型而不是引用类型。这意味着当数组赋值给一个新的变量时，
func TestArrayAreValueTypes(t *testing.T) {
	a := [...]string{"USA", "China", "India", "Germany", "France"}

	// 该变量会得到一个原始数组的一个副本。如果对新变量进行更改，则不会影响原始数组。
	b := a
	b[0] = "Singapore"
	fmt.Println("a is", a)
	fmt.Println("b is", b)
}

// 同样当数组作为参数传递给函数时，它们是按值传递，而原始数组保持不变。
func TestArrayPassToFunction(t *testing.T) {
	num := [...]int{5, 6, 7, 8, 9}
	t.Log("before passing to function", num)
	changeLocal(num)
	t.Log("after passing to function", num)
}

// 数组是按值传递
func changeLocal(num [5]int) {
	num[0] = 55
	fmt.Println("inside function", num)
}

// 遍历数组
func TestIteratingArray(t *testing.T) {
	// 第一种使用for
	a := [...]float64{67.7, 89.8, 54, 72}
	for i := 0; i < len(a); i++ {
		t.Logf("%d the element of a is %.2f\n", i, a[i])
	}

	t.Log("for range:")
	// 第二种使用 for range
	for i, v := range a {
		t.Logf("%d the element of a is %.2f\n", i, v)
	}

	// 如果你只需要值并希望忽略索引，则可以通过用 _ 空白标识符替换索引来执行。
	// for _, v := range a { // ignores index
	// }

}

// 多维数组
func TestMultidimessionalArray(t *testing.T) {
	// 简单声明并初始化
	a := [3][2]string{
		{"lion", "tiger"},
		{"cat", "dog"},
		{"pigeon", "peacock"}, // 此处的逗号，必须要有，否则Go会自动插入分号，导致编译错误
	}
	printarray(a)

	// 先声明后赋值
	var b [3][2]string
	b[0][0] = "apple"
	b[0][1] = "samsung"
	b[1][0] = "microsoft"
	b[1][1] = "google"
	b[2][0] = "baidu"
	b[2][1] = "huawei"
	printarray(b)
}

func printarray(a [3][2]string) {
	for _, v1 := range a {
		for _, v2 := range v1 {
			fmt.Printf("%s ", v2)
		}
		fmt.Printf("\n")
	}
}
