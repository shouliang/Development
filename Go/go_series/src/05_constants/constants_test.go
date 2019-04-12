package constants

import (
	"testing"
)

// const declares a constant value.

// 常量不能再重新赋值为其他的值。
// 因此下面的程序将不能正常工作，它将出现一个编译错误: cannot assign to a.
func TestCanNotChangedConstant(t *testing.T) {
	// const a = 55
	// a = 89 // 不允许重新赋值
}

// 常量的值会在编译的时候确定。因为函数调用发生在运行时，所以不能将函数的返回值赋值给常量。
func TestCanNotAssignVariable(t *testing.T) {
	// var a = math.Sqrt(4)  // 允许
	// const b = math.Sqrt(4) // 不允许 const initializer math.Sqrt(4) is not a constant
}

// 字符串常量
func TestStringConstants(t *testing.T) {
	const hello = "hello world"

	// 常量 hello 有类型吗？答案是没有
	// 无类型的常量有一个与它们相关联的默认类型。
	// 它从字符串常量 hello world 的默认类型中获取。
	t.Logf("Type of hell %T", hello)

	// 创建一个带类型的常量
	const typedhello string = "hello world"
	t.Logf("Type of typedhello %T", typedhello)

	// Go 是一个强类型的语言，在分配过程中混合类型是不允许的
	// var defaultName = "Sam"         // 允许
	// type myString string            // 自定义一个新类型myString
	// var customName myString = "Sam" // 允许：因常量Sam是无类型的，可以分配给任何字符串变量
	//
	// // cannot use defaultName (type string) as type myString in assignment
	// customName = defaultName // 不允许：类型不一致，defaultName是string类型，customName是myString类型，
}

// 布尔常量
func TestBoolConstants(t *testing.T) {
	// const trueConst = true
	// type myBool bool
	// var defualtBool = trueConst       // 允许
	// var customBool myBool = trueConst // 允许
	//
	// // cannot use customBool (type myBool) as type bool in assignment
	// defualtBool = customBool // 不允许： 类型不一致

}

// 数量常量
// 常量 a 是没有类型的，它的值是 5 。您可能想知道 a 的默认类型是什么，如果它确实有一个的话, 那么我们如何将它分配给不同类型的变量。
func TestNumericConstant(t *testing.T) {
	const a = 5
	var intVar int = a
	var int32Var int32 = a
	var float64Var float64 = a
	var complex64Var complex64 = a
	t.Log("intVar", intVar, "\nintint32Var", int32Var, "\nfloat64Var", float64Var, "\ncomplex64Var", complex64Var)
}

// 数字表达式
// 数字常量可以在表达式中自由混合和匹配，
// 只有当它们被分配给变量或者在需要类型的代码中的任何地方使用时，才需要类型。
func TestNumericExpression(t *testing.T) {
	var a = 5.9 / 8
	t.Logf("a's type is %T value %v", a, a)
}
