// 常量
package constant_test

import "testing"

const (
	Monday = 1 + iota // 特殊常量，每新增一行常量声明将使iota计数加1
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
	Sunday
)

const (
	Readable = 1 << iota
	Writable
	Executable
)

func TestConstantTry(t *testing.T) {
	t.Log(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
}

func TestConstantTry02(t *testing.T) {
	a := 1 // 0001
	t.Log(Readable, Writable, Executable)
	t.Log(a&Readable == Readable, a&Writable == Writable, a&Executable == Executable)
	a = 7 // 0111
	t.Log(a&Readable == Readable, a&Writable == Writable, a&Executable == Executable)
}
