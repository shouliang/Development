package pointers

import "testing"

// 指针的声明
// 指针变量的类型为 *T，该指针指向一个 T 类型的变量。
func TestDeclaringPointer(t *testing.T) {
	b := 255

	// & 操作符用于获取变量的地址
	var a *int = &b
	t.Logf("Type of a is %T\n", a)
	t.Log("address of b is", a)
}

// 指针的零值 nil
func TestZeroValueOfPointer(t *testing.T) {
	a := 25
	var b *int
	if b == nil {
		t.Log("b is", b)
		b = &a
		t.Log("b after initialization is", b)
	}
}

// 指针的解引用
// 指针的解引用可以获取指针所指向的变量的值。将 a 解引用的语法是 *a
func TestDereferencingAPointer(t *testing.T) {
	b := 255
	a := &b
	t.Log("address of b is", a)

	// *a 可以将a解引用，等到b的值
	t.Log("value of b is", *a)

	// 把 a 指向的值加 1，由于 a 指向了 b，因此 b 的值也发生了同样的改变
	*a++
	t.Log("new value of b is", b)
}

func change(val *int) {
	*val = 255
}

// 向函数传递指针参数
func TestPassPointerToAFunction(t *testing.T) {
	a := 58
	t.Log("value of a before function call is", a)
	b := &a

	// 我们向函数 change 传递了指针变量 b，而 b 存储了 a 的地址。
	// 在 change 函数内使用解引用，修改了 a 的值
	change(b)
	t.Log("value of a after function call is", a)
}

// 向函数传递数组的指针
func modifyPassByArray(arr *[3]int) {
	(*arr)[0] = 999

	// a[x] 是 (*a)[x] 的简写形式，因此上面代码中的 (*arr)[0] 可以替换为 arr[0]
	//arr[0] = 999
}

// 向函数传递切片
func modifyPassBySlice(sls []int) {
	sls[1] = 888
}

// 不要向函数传递数组的指针，而应该使用切片
// 这种方式向函数传递一个数组指针参数，并在函数内修改数组。尽管它是有效的，
// 但却不是 Go 语言惯用的实现方式。我们最好使用切片来处理。
func TestPassPointerSliceInsteadOfArray(t *testing.T) {
	a := [3]int{1, 2, 3}

	// 向函数传递数组的指针
	modifyPassByArray(&a)
	t.Log(a)

	// 向函数传递切片
	modifyPassBySlice(a[:])
	t.Log(a)
}

// Go 不支持指针运算
func TestDoNotSupportPointerArithmetic(t *testing.T) {
	b := [...]int{1, 2, 3}
	p := &b
	t.Log(p)
	// p++  // invalid operation: p++ (non-numeric type *[3]int)
}
