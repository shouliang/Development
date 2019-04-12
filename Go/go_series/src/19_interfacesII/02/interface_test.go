package interfaceII02

import (
	"fmt"
	"testing"
)

// 实现多个接口

type SalaryCalculator interface {
	DisplaySalary()
}

type LeaveCalculator interface {
	CalculateLeavesLeft() int
}

type Employee struct {
	firstName   string
	lastName    string
	basicPay    int
	pf          int
	totalLeaves int
	leavesTaken int
}

// 实现了 SalaryCalculator 接口的 DisplaySalary 方法
func (e Employee) DisplaySalary() {
	fmt.Printf("%s %s has salary $%d\n", e.firstName, e.lastName, (e.basicPay + e.pf))
}

// 实现了 LeaveCalculator 接口里的 CalculateLeavesLeft 方法
func (e Employee) CalculateLeavesLeft() int {
	return e.totalLeaves - e.leavesTaken
}

func TestMultiInterface(t *testing.T) {
	e := Employee{
		firstName:   "Naveen",
		lastName:    "Ramanathan",
		basicPay:    5000,
		pf:          200,
		totalLeaves: 30,
		leavesTaken: 5,
	}

	// e 赋值给了 SalaryCalculator 类型的接口变量
	var s SalaryCalculator = e
	s.DisplaySalary()

	// 把 e 赋值给 LeaveCalculator 类型的接口变量
	var l LeaveCalculator = e
	t.Log("\n Leaves left =", l.CalculateLeavesLeft())
}
