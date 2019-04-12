package interface04

import (
	"fmt"
	"testing"
)

func assert(i interface{}) {
	s := i.(int)
	fmt.Println(s)
}

func assertWithOK(i interface{}) {
	v, ok := i.(int)
	fmt.Println(v, ok)
}

/*类型断言
类型断言用于提取接口的底层值（Underlying Value）。
在语法 i.(T) 中，接口 i 的具体类型是 T，该语法用于获得接口的底层值
*/

func TestAssert(t *testing.T) {
	var i interface{} = 56
	assert(i)

	// 传递的不是int类型的会报错
	// panic: interface conversion: interface {} is string, not int
	// var s interface{} = "Steven"
	// assert(s)

	// 要解决该问题，我们可以使用以下语法：
	// v, ok := i.(T)

	var s interface{} = "Steven"
	// s 的具体类型不是 int，ok 赋值为 false，而 v 赋值为 0（int 的零值
	assertWithOK(s)
}

/* 类型选择（Type Switch）
类型选择用于将接口的具体类型与很多 case 语句所指定的类型进行比较。它与一般的 switch 语句类似。
唯一的区别在于类型选择指定的是类型，而一般的 switch 指定的是值。
类型选择的语法类似于类型断言。类型断言的语法是 i.(T)，而对于类型选择，类型 T 由关键字 type 代替
*/
func TestFindType(t *testing.T) {
	findType("zhangsan")
	findType(77)
	findType(88.99)
}

func findType(i interface{}) {
	switch i.(type) {
	case string:
		fmt.Printf("I am a string and my value is %s\n", i.(string))
	case int:
		fmt.Printf("I am a int and my value is %d\n", i.(int))
	default:
		fmt.Printf("Unknown type\n")
	}
}
