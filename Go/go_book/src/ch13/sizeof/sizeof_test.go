package sizeof_test

import (
	"testing"
	"unsafe"
)

func Test(t *testing.T) {
	var x struct {
		a bool
		b int16
		c []int
	}
	t.Log(unsafe.Sizeof(x), unsafe.Alignof(x))
	t.Log(unsafe.Sizeof(x.a), unsafe.Alignof(x.a), unsafe.Offsetof(x.a))
	t.Log(unsafe.Sizeof(x.b), unsafe.Alignof(x.b), unsafe.Offsetof(x.b))
	t.Log(unsafe.Sizeof(x.c), unsafe.Alignof(x.c), unsafe.Offsetof(x.c))
}
