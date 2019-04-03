// 基本类型
// Go 的基本类型有
// bool
// string
// int int8 int16 int32 uint64
// uint uint8 uint16 uint32 uint64 uintptr
// byte // uint8的别名
// rune // int32的别名 代表一个Unicode码
// float32 float64
// complex64 complex128
package main

import (
	"fmt"
	"math/cmplx"
)

var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func main() {
	const f = "%T(%v)\n"
	fmt.Printf(f, ToBe, ToBe)
	fmt.Printf(f, MaxInt, MaxInt)
	fmt.Printf(f, z, z)
}
