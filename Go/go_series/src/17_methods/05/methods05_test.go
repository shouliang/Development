package methodstest05

import "testing"

/* 在非结构体上的方法
为了在一个类型上定义一个方法，方法的接收器类型定义和方法的定义应该在同一个包中。
到目前为止，我们定义的所有结构体和结构体上的方法都是在同一个 main 包中，因此它们是可以运行的。
*/

/*
我们尝试把一个 add 方法添加到内置的类型 int。
这是不允许的，因为 add 方法的定义和 int 类型的定义不在同一个包中。
该程序会抛出编译错误 cannot define new methods on non-local type int。

func (a int) add(b int) {

}
*/

// 为内置类型 int 创建一个类型别名，然后创建一个以该类型别名为接收器的方法。
type myInt int

func (a myInt) add(b int) int {
	return int(a) + b
}

func TestMethodsOnNonStruct(t *testing.T) {
	num1 := myInt(5)
	sum := num1.add(6)
	t.Log("sum is", sum)
}
