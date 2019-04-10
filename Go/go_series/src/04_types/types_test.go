package types

import (
	"testing"
	"unsafe"
)

// bool类型
// bool 类型表示一个布尔值，值为 true 或者 false。
func TestBool(t *testing.T) {
	a := true
	b := false
	t.Log("a:", a, "b:", b)
}

// 有符号整型: int8: int16 int32 int64
/* int8: -128~127 ?
最高位0，表示正数，故8位的最大正数为01111111 = 2的7次方 - 1 = 127
最高位1，表示负数，负数在计算机中以补码的形式存储
最大的负数-1的补码为:11111111
	1、先取-1的原码：     10000001
	2、除符号位取反得反码: 11111110
	3、加1得补码：        11111111
-2的补码为-1减去1，即11111111 -1 =11111110，直到减去除符号位的所有1得到最小的负数即 10000000 = -128
*/
// int：根据不同的底层平台（Underlying Platform），表示 32 或 64 位整型。
// 除非对整型的大小有特定的需求，否则你通常应该使用 int 表示整型。
// int类型大小：在 32 位系统下是 32 位，而在 64 位系统下是 64 位。
func TestInt(t *testing.T) {
	var a int = 89
	b := 95
	t.Log("value of a is", a, "and b is", b)

	// unsafe 包提供了一个 Sizeof 函数，该函数接收变量并返回它的字节大小
	t.Logf("type of a is %T, size of a is %d\n", a, unsafe.Sizeof(a))
	t.Logf("type of b is %T, size of b is %d\n", b, unsafe.Sizeof(b))
}

// 浮点型
func TestFloat(t *testing.T) {
	a, b := 5.67, 1.28
	// 和 b 的类型根据赋值推断得出。在这里，a 和 b 的类型为 float64（float64 是浮点数的默认类型）
	t.Logf("type of a %T b %T", a, b)
}

// 复数类型
// 内建函数 complex 用于创建一个包含实部和虚部的复数。complex 函数的定义如下：
// 																				func complex(r, i FloatType) ComplexType
func TestComplex(t *testing.T) {
	c1 := complex(5, 7)
	c2 := 8 + 27i
	cadd := c1 + c2
	t.Log("sum:", cadd)

	cmul := c1 * c2
	t.Log("product:", cmul)
}

// 类型转换
func TestTypeConversion(t *testing.T) {
	i := 55
	j := 67.8
	t.Logf("type of i %T j %T", i, j)

	//不允许 int + float64
	// sum := i + j // mismatched types int and float64
	// 要修复这个错误，i 和 j 应该是相同的类型。在这里，我们把 j 转换为 int 类型。把 v 转换为 T 类型的语法是 T(v)。
	sum := i + int(j)
	t.Log(sum)
}

// 显示的类型转换
// 把一个变量赋值给另一个不同类型的变量，需要显式的类型转换
func TestExplicitConversion(t *testing.T) {
	i := 10
	var j float64 = float64(i)
	t.Log("j is", j)
}
