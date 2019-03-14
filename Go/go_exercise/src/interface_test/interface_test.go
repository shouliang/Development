package interface_test

import (
	"testing"
)

// 子接口
type stringer interface {
	string() string
}

// 超接口
type tester interface {
	stringer // 接口中嵌入其他接口
	test()
	stringother() string
}

type data struct{}

func (*data) test()              {}
func (data) string() string      { return "just string" }
func (data) stringother() string { return "just stringother" }

// 参数为子接口类型，可以接受超接口类型
func pp(a stringer) string {
	return a.string()
}

func TestInterFace(t *testing.T) {
	var d data

	var te tester
	// te = d // data does not implement tester (test method has pointer receiver)
	te = &d
	te.test()
	t.Log(te.stringother())
}

func TestInterFaceNil(t *testing.T) {
	var t1, t2 interface{}     // 空接口类似面对对象的根类型Object
	t.Log(t1 == nil, t1 == t2) // 接口类型默认值是nil

	t1, t2 = 100, 100
	t.Log(t1 == t2)

	// t1, t2 = map[string]int{}, map[string]int{}
	// t.Log(t1 == t2) // map类型不支持接口实现
}

func TestSuperComplictToSub(t *testing.T) {
	var d data
	var te tester = &d
	t.Log(pp(te)) // 隐式转换成子集

	var s stringer = te // 超集转换成子集
	t.Log(s.string())

	// var t2 tester = s // stringer does not implement tester (missing stringother method)

}
