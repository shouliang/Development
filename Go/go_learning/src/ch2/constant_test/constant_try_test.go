package constant_test

import "testing"

const (
	Monday = 1 + iota
	Tuesday
	Wednesday
)

const (
	Readable = 1 << iota
	Writable
	Executable
)

func TestConstantTry(t *testing.T) {
	t.Log(Monday, Tuesday)
}

func TestConstantTry02(t *testing.T) {
	a := 1 // 0001
	t.Log(Readable, Writable, Executable)
	t.Log(a&Readable == Readable, a&Writable == Writable, a&Executable == Executable)
	a = 7 // 0111
	t.Log(a&Readable == Readable, a&Writable == Writable, a&Executable == Executable)
}
