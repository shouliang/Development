package unsafettest

import (
	"testing"
	"unsafe"
)

func TestUnSafe(t *testing.T) {
	i := 10
	f := *(*float64)(unsafe.Pointer(&i))
	t.Log(unsafe.Pointer(&i))
	t.Log(f)
}

type MyInt int

// 合理的类型转换
func TestConvert(t *testing.T) {
	a := []int{1, 2, 4}
	b := *(*[]MyInt)(unsafe.Pointer(&a))
	t.Log(b)
}
