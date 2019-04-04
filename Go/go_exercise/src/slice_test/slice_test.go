package slice_test

import "testing"

func TestSlice(t *testing.T) {
	a := [5]int{1, 2, 3, 4, 5}
	b := a[:]
	c := a[0:3]
	t.Logf("a type is %T\n", a) // [5]int 数组类型
	t.Logf("b type is %T\n", b) // 切片类型
	t.Logf("c type is %T\n", c) // 切片类型
}
