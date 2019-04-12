package interfaceII03

import (
	"fmt"
	"testing"
)

/* 接口的嵌套
尽管 Go 语言没有提供继承机制，但可以通过嵌套其他的接口，创建一个新接口。
我们来看看这如何实现。
*/

type SalaryCalculator interface {
	DisplaySalary()
}

type LeaveCalculator interface {
	CalculateLeavesLeft() int
}

//一个新的接口 EmployeeOperations，它嵌套了两个接口：SalaryCalculator 和 LeaveCalculator。
type EmployeeOperations interface {
	SalaryCalculator
	LeaveCalculator
}

type Employee struct {
	firstName   string
	lastName    string
	basicPay    int
	pf          int
	totalLeaves int
	leavesTaken int
}

func (e Employee) DisplaySalary() {
	fmt.Printf("%s %s has salary $%d\n", e.firstName, e.lastName, (e.basicPay + e.pf))
}

func (e Employee) CalculateLeavesLeft() int {
	return e.totalLeaves - e.leavesTaken
}

func TestEmbeddingInterfaces(t *testing.T) {
	e := Employee{
		firstName:   "Naveen",
		lastName:    "Ramanathan",
		basicPay:    5000,
		pf:          200,
		totalLeaves: 30,
		leavesTaken: 5,
	}
	// 由于 Employee 结构体定义了 DisplaySalary 和 CalculateLeavesLeft 方法，
	// 因此它实现了接口 EmployeeOperations。
	var empOp EmployeeOperations = e

	empOp.DisplaySalary()
	t.Log("Leaves left =", empOp.CalculateLeavesLeft())
}
