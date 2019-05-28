package encapsulation

import (
	"fmt"
	"testing"
)

type Employee struct {
	Id   string
	Name string
	Age  int
}

// 第一种 定义方式在实例对应方法被调用时，实例的成员会进行值复制
func (e Employee) String1() string {
	fmt.Printf("Address is of e.Name in String1() is %x\n", &e.Name)
	return fmt.Sprintf("Id:%s-Name:%s-Age:%d", e.Id, e.Name, e.Age)
}

// 第二种 通常情况下为了避免内存拷贝会使用这种方式
func (e *Employee) String2() string {
	fmt.Printf("Address is of e.Name in String2() is %x\n", &e.Name)
	return fmt.Sprintf("Id:%s/Name:%s/Age:%d", e.Id, e.Name, e.Age)
}

func TestCreateEmployeeObj(t *testing.T) {
	e := Employee{"0", "Bob", 20}
	e1 := Employee{Name: "Mike", Age: 30}

	// 返回指针
	e2 := new(Employee)
	// 指针类型访问成员变量，不需要箭头符号->,依然是通过.即可
	e2.Id = "2"
	e2.Name = "Rose"

	t.Log("e is ", e)
	t.Log("e1 is ", e1)

	// 默认值为空字符串 ""
	t.Log("e1.Id is", e1.Id)
	t.Log("e2 is ", e2)

	t.Logf("type of e is %T", e)
	// *encapsulation.Employee指针类型
	t.Logf("type of e2 is %T", e2)

}

func TestStructOperations(t *testing.T) {
	e := Employee{"3", "Mary", 23}
	t.Logf("Address is of e.Name is %x\n", &e.Name)
	t.Log(e.String1())
	t.Log(e.String2())

	// e1 := &Employee{"2", "Lucy", 24}
	// t.Logf("Address is of e1.Name is %x\n", &e1.Name)
	// t.Log(e1.String1())
	// t.Log(e1.String2())
}
