package interface03

import (
	"fmt"
	"testing"
)

// 接口的内部表示
// 我们可以把接口看作内部的一个元组 (type, value)。

type Test interface {
	Tester()
}

type MyFloat float64

func (m MyFloat) Tester() {
	fmt.Println(m)
}

func describe(t Test) {
	fmt.Printf("Interface type %T value %v \n", t, t)
}

// Test 接口只有一个方法 Tester()，而 MyFloat 类型实现了该接口
func TestInterfaceInternal(t *testing.T) {
	var test Test
	f := MyFloat(89.7)

	// 把变量 f（MyFloat 类型）赋值给了 t（Test 类型）。
	// 现在 t 的具体类型为 MyFloat，而 t 的值为 89.7
	test = f

	describe(test)
	test.Tester()
}

/*空接口
没有包含方法的接口称为空接口。空接口表示为 interface{}。
由于空接口没有方法，因此所有类型都实现了空接口。
*/
func TestVoidInterface(t *testing.T) {
	s := "Hello World"
	describeInterface(s)

	i := 55
	describeInterface(i)

	strt := struct {
		name string
	}{
		name: "zhangsan",
	}
	describeInterface(strt)
}

// 函数接收空接口作为参数，因此，可以给这个函数传递任何类型
func describeInterface(i interface{}) {
	fmt.Printf("Type = %T,value = %v\n", i, i)
}
