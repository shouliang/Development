package mapext

import "testing"

func TestMapWithFunValue(t *testing.T) {
	m := map[int]func(op int) int{} // map可以为int ,value为一个方法,实现工厂模式

	m[1] = func(op int) int { return op }
	m[2] = func(op int) int { return op * op }
	m[3] = func(op int) int { return op * op * op }

	t.Log(m[1](2), m[2](2), m[3](2))
}

// go语言里面没有set类型，理由map来实现set的特性
func TestMapForSet(t *testing.T) {
	mySet := map[int]bool{}
	mySet[1] = true

	n := 1
	if mySet[n] {
		t.Logf("%d is existing", n)
	} else {
		t.Logf("%d is existing", n)
	}
	mySet[5] = false
	t.Log(len(mySet))

	delete(mySet, 1)
	if mySet[n] {
		t.Logf("%d is existing", n)
	} else {
		t.Logf("%d is existing", n)
	}
}
