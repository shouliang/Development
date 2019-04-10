package variables

import "testing"

// 声明单个变量
// var name type 是声明单个变量的语法。
func TestDeclaringASingleVariable(t *testing.T) {
	// 如果变量未被赋值，Go 会自动地将其初始化，
	// 赋值该变量类型的零值（Zero Value）,本例中 age 就被赋值为 0
	var age int
	t.Log("my age is", age)

	// 变量可以赋值为本类型的任何值
	age = 29
	t.Log("my age is", age)
	age = 54
	t.Log("my newage is", age)
}

// 声明变量并初始化
// 声明变量的同时可以给定初始值。
// var name type = initialvalue 的语法用于声明变量并初始化。
func TestDeclaringAndInitial(t *testing.T) {
	// 声明变量并初始化
	var age int = 29
	t.Log("my initial age is", age)
}

// 类型推断（Type Inference）
// 如果变量有初始值，那么 Go 能够自动推断具有初始值的变量的类型。因此，如果变量有初始值，就可以在变量声明中省略 type。
// 如果变量声明的语法是 var name = initialvalue，Go 能够根据初始值自动推断变量的类型。
func TestTypeInference(t *testing.T) {
	// 省略了变量 age 的 int 类型，Go 依然推断出了它是 int 类型。
	var age = 60
	t.Logf("my age Type is %T", age)
}

// 声明多个变量
// 声明多个变量的语法是 var name1, name2 type = initialvalue1, initialvalue2。
func TestDeclareMultiVariables(t *testing.T) {
	var width, height int = 100, 500
	t.Log("width is", width, "height is", height)
}

// 声明多个变量：未初始化
func TestDeclareMultiVariablesNotInitial(t *testing.T) {
	// 如果 width 和 height 省略了初始化，它们的初始值将赋值为 0
	var width, height int
	t.Log("width is", width, "height is", height)
}

// 声明多个变量：未初始化
/* 在有些情况下，我们可能会想要在一个语句中声明不同类型的变量。其语法如下：

var (
    name1 = initialvalue1
    name2 = initialvalue2
)
*/
func TestDeclareMultiVariablesDifferentType(t *testing.T) {
	var (
		name   = "Jack"
		age    = 24
		height int
	)
	t.Log("my name is", name, "age is", age, "and height is", height)
}

// 简短声明
// 声明变量的简短语法是 name := initialvalue
func TestShortHandDeclaration(t *testing.T) {
	name, age := "Lucy", 29
	t.Log("my name is", name, "age is", age)

	// 简短声明要求 := 操作符左边的所有变量都有初始值,否则会报错
	// x, y := "x"  // assignment mismatch: 2 variable but 1 values

	// 简短声明的语法要求 := 操作符的左边至少有一个变量是尚未声明的。
	a, b := 20, 30
	t.Log("a is", a, "b is", b)
	b, c := 40, 50 // b已经声明，但c尚未声明
	t.Log("b is", b, "c is", c)

	x, y := 99, 100
	t.Log("x is", x, "y is", y)
	// 因为 x 和 y 的变量已经声明过了，:= 的左边并没有尚未声明的变量，所以会报错
	// x, y := 1, 2 // no new variables on left side of :=

	//由于 Go 是强类型（Strongly Typed）语言，因此不允许某一类型的变量赋值为其他类型的值
	// xxx := 66
	// xxx = "xxx" // cannot use "xxx" (type string) as type int in assignment
}
