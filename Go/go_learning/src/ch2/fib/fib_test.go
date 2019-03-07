package fib

import "testing"

func TestFibList(t *testing.T) {
	// var a int = 1
	// var b int = 1

	// var (
	//   a int = 1
	//   b int = 1
	// )

	a := 1 // 变量初始化的一种，可以进行自动类型推断
	b := 1

	t.Log(a)
	for i := 0; i < 5; i++ {
		t.Log(" ", b)
		tmp := a
		a = b
		b = tmp + a
	}
}

func TestExchange(t *testing.T) {
	a := 1
	b := 3

	// tmp := a
	// a = b
	// b = tmp
	a, b = b, a // 在一个复制语句中可以对多个变量进行同时赋值

	t.Log(a, b)
}
