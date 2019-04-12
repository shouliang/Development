package methodstest02

import "testing"

type Employee struct {
	name string
	age  int
}

/* 指针接收器与值接收器
可以创建使用指针接收器的方法。
值接收器和指针接收器之间的区别在于，
在指针接收器的方法内部的改变对于调用者是可见的，然而值接收器不可见
*/

/*
那么什么时候使用指针接收器，什么时候使用值接收器？
一般来说，指针接收器可以使用在：对方法内部的接收器所做的改变应该对调用者可见时。

指针接收器也可以被使用在如下场景：当拷贝一个结构体的代价过于昂贵时。
考虑下一个结构体有很多的字段。在方法内使用这个结构体做为值接收器需要拷贝整个结构体，
这是很昂贵的。在这种情况下使用指针接收器，结构体不会被拷贝，只会传递一个指针到方法内部使用。
*/

// 使用值接收器的方法。
func (e Employee) changeName(newName string) {
	e.name = newName
}

// 使用指针接收器的方法。
func (e *Employee) changeAge(newAge int) {
	e.age = newAge
}

func TestValueReceiversAndPointerReceivers(t *testing.T) {
	e := Employee{
		name: "Jack",
		age:  25,
	}
	// name not changed
	t.Logf("Employee name before change: %s\n", e.name)
	e.changeName("Steve")
	t.Logf("Employee name after change: %s\n", e.name)

	// age had changed
	t.Logf("Employee age before change: %d\n", e.age)
	(&e).changeAge(26)
	// 由于 changeAge 方法有一个指针接收器，所以我们使用 (&e) 来调用这个方法。
	// 其实没有这个必要，Go语言让我们可以直接使用 e.changeAge(51)。
	// e.changeAge(51) 会自动被Go语言解释为 (&e).changeAge(51)。
	// e.changeAge(26)
	t.Logf("Employee age after change: %d\n", e.age)
}
