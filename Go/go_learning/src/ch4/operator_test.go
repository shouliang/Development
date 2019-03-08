package operator_test

import "testing"

const (
	Readable = 1 << iota
	Writable
	Executable
)

func TestCompareArray(t *testing.T) {
	a := [...]int{1, 2, 3, 4}
	b := [...]int{1, 3, 2, 5}
	// c := [...]int{1, 2, 3, 4,5}
	d := [...]int{1, 2, 3, 4}

	t.Log(a == b)
	t.Log(a == d) // 数组个数相同且对应位置的元素相等，则两个数组也相等
}

func TestBitClear(t *testing.T) {
	a := 7 // 0111
	a = a &^ Readable
	t.Log(a&Readable == Readable)
}
