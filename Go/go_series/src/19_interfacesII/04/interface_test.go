package interfaceII04

import "testing"

// 接口的零值
type Describer interface {
	Describe()
}

// 接口的零值是 nil。对于值为 nil 的接口，
// 其底层值（Underlying Value）和具体类型（Concrete Type）都为 nil。
func TestInterfaceZeroValue(t *testing.T) {
	var d1 Describer
	if d1 == nil {
		t.Logf("d1 is nil and has type %T value %v\n", d1, d1)
	}

	// 对于值为 nil 的接口，由于没有底层值和具体类型，
	// 当我们试图调用它的方法时，程序会产生 panic 异常。
	d1.Describe()
}
