package func_test

import "testing"

// 单一返回值
// 多返回值
// func 回传 func
// Anonymous Func(常使用在 go routine)
// func 参数设计

func add(a, b int) int {
	return a + b
}

func swap(a, b int) (int, int) {
	return b, a
}

func foo() func() int {
	return func() int {
		return 100
	}
}

func TestFunc(t *testing.T) {
	t.Log(add(2, 5))

	a := 1
	b := 2
	a, b = swap(a, b)
	t.Log(a, b)

	a, b = b, a
	t.Log(a, b)

	funcfoo := foo()
	t.Logf("%T", funcfoo)
	t.Log(funcfoo())

	bar := func(a, b float32) float32 {
		return a + b
	}

	t.Logf("%T", bar)
	t.Log(bar(1.3, 2.5))

	// 匿名函数自己执行
	func() {
		t.Log("Hello from Anonymous func")
	}()

	func(a, b int) int {
		return a + b
	}(4, 5)
	
}
