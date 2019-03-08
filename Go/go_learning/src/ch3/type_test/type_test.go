// 数据类型
package type_test

import "testing"

type MyInt int64 // 定义一个类型别名

func TestImplicit(t *testing.T) {
	var a int32 = 1
	var b int64
	// b = a      // 不支持隐式类型转换
	b = int64(a)

	var c MyInt
	// c = b    // 别名和原有类型也不支持进行隐式类型转换
	c = MyInt(b)
	t.Log(a, b, c)
}

func TestPoint(t *testing.T) {
	a := 1
	aPtr := &a
	// aPtr = aPtr + 1 // 指针不支持运算
	t.Log(a, aPtr)
	t.Logf("%T %T", a, aPtr) // %T 输出类型
}

func TestString(t *testing.T) {
	var s string
	t.Log("*" + s + "*") // string是值类型，默认值为空字符串
	t.Log(len(s))
}
