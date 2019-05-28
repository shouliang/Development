package interview_test

import (
	"errors"
	"fmt"
	"reflect"
	"testing"
)

type People interface {
	Show()
}

type Student struct{}

func (stu *Student) Show() {

}

func live() People {
	var stu *Student
	return stu
}

func TestInterface(t *testing.T) {
	if live() == nil {
		t.Log("AAAAAAA")
	} else {
		t.Log("BBBBBBB")
	}
}

// func TestType(t *testing.T) {
// 	i := GetValue()
// 	// 编译失败，因为type只能使用在interface
// 	switch i.(type) {
// 	case int:
// 		println("int")
// 	case string:
// 		println("string")
// 	case interface{}:
// 		println("interface")
// 	default:
// 		println("unknown")
// 	}

// }

// func GetValue() int {
// 	return 1
// }

// 此处函数第一个返回值有sum名称，第二个未命名，所以错误。
// func funcMui(x,y int)(sum int,error){
//     return x+y,nil
// }

func funcMui(x, y int) (sum int, e error) {
	return x + y, nil
}

func TestDeferFunc(t *testing.T) {
	t.Log(DeferFunc1(1))
	t.Log(DeferFunc2(1))
	t.Log(DeferFunc3(1))
}

func DeferFunc1(i int) (t int) {
	t = i
	defer func() {
		t += 3
	}()
	return t
}

func DeferFunc2(i int) int {
	t := i
	defer func() {
		t += 3
	}()
	return t
}

func DeferFunc3(i int) (t int) {
	defer func() {
		t += i
	}()
	return 2
}

func TestSliceNew(t *testing.T) {
	// list := new([]int)
	list := make([]int, 0)
	list = append(list, 1)
	t.Log(list)

	s1 := []int{1, 2, 3}
	s2 := []int{4, 5}
	// s1 = append(s1, s2)
	s1 = append(s1, s2...)
	t.Log(s1)
}

func TestStructEqual(t *testing.T) {
	sn1 := struct {
		age  int
		name string
	}{age: 11, name: "qq"}
	sn2 := struct {
		age  int
		name string
	}{age: 11, name: "qq"}

	if sn1 == sn2 {
		t.Log("sn1 == sn2")
	}
	// 进行结构体比较时候，只有相同类型的结构体才可以比较，结构体是否相同不但与属性类型个数有关，还与属性顺序相关。
	// sn3 := struct {
	// 	name string
	// 	age  int
	// }{name: "qq", age: 11}
	// if sn1 == sn3 {
	// 	t.Log("sn1 == sn3")
	// }

	// 还有一点需要注意的是结构体是相同的，但是结构体属性中有不可以比较的类型，如map,slice。
	// 如果该结构属性都是可以比较的，那么就可以使用“==”进行比较操作。
	sm1 := struct {
		age int
		m   map[string]string
	}{age: 11, m: map[string]string{"a": "1"}}
	sm2 := struct {
		age int
		m   map[string]string
	}{age: 11, m: map[string]string{"a": "1"}}

	// if sm1 == sm2 {
	// 	t.Log("sm1 == sm2")
	// }

	if reflect.DeepEqual(sm1, sm2) {
		t.Log("sm1 == sm2 in DeepEqual")
	}
}

func Foo(x interface{}) {
	if x == nil {
		fmt.Println("empty interface")
		return
	}
	fmt.Println("non-empty interface")
}
func TestInterfaceEmpty(t *testing.T) {
	var x *int = nil
	Foo(x)
}

const (
	x = iota
	y
	z = "zz"
	k
	p = iota
)

func TestConst(t *testing.T) {
	t.Log(x, y, z, k, p)
}

const cl = 100

var bl = 123

func TestConstantAddress(t *testing.T) {
	t.Log(&bl, bl)

	//常量不同于变量的在运行期分配内存，常量通常会被编译器在预处理阶段直接展开，作为指令数据使用，
	// t.Log(&cl,cl) // cannot take the address of cl
}

func TestDefinition(t *testing.T) {
	type MyInt1 int   // 定义新类型
	type MyInt2 = int // 别名
	var i int = 9
	// var i1 MyInt1 = i // 不同的类型，需要转换
	var i1 MyInt1 = MyInt1(i)
	var i2 MyInt2 = i
	t.Log(i1, i2)
}

var ErrDidNotWork = errors.New("did not work")

func DoTheThing(reallyDoIt bool) (err error) {
	if reallyDoIt {
		// result, err := tryTheThing() // if 语句块内的 err 变量会遮罩函数作用域内的 err 变量
		var result string
		result, err = tryTheThing()
		if err != nil || result != "it worked" {
			err = ErrDidNotWork
		}
	}
	return err
}

func tryTheThing() (string, error) {
	return "", ErrDidNotWork
}

func TestErrors(t *testing.T) {
	t.Log(DoTheThing(true))
	t.Log(DoTheThing(false))
}

func test() []func() {
	var funs []func()
	for i := 0; i < 2; i++ {
		funs = append(funs, func() {
			println(&i, i) // 闭包延迟求值，使用了外部变量i
		})
	}
	return funs
}

func TestF(t *testing.T) {
	funs := test()
	for _, f := range funs {
		f()
	}
}
