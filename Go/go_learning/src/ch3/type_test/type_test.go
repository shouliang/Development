// 数据类型
package type_test

import "testing"

// 定义一个类型别名
type MyInt int64

func TestImplicit(t *testing.T) {
	var a int32 = 1
	var b int64

	// 不支持隐式类型转换
	// b = a
	b = int64(a)

	var c MyInt

	// 别名和原有类型也不支持进行隐式类型转换
	// c = b

	c = MyInt(b)
	t.Log(a, b, c)
}

func TestPoint(t *testing.T) {
	a := 1
	aPtr := &a

	// 指针不支持运算
	// aPtr = aPtr + 1
	t.Log(a, aPtr)

	// %T 输出类型
	t.Logf("%T %T", a, aPtr)
}

func TestString(t *testing.T) {
	var s string

	// string是值类型，默认值为空字符串
	t.Log("*" + s + "*")
	t.Log(len(s))
}
