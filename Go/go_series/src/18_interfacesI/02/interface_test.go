package inteface02

import (
	"fmt"
	"testing"
)

// 接口的实际用途

// 定义接口:
type SalaryCalculator interface {
	CalculateSalary() int
}

// 长期员工
type Permanent struct {
	empId    int
	basicPay int
	pf       int
}

// 合同工
type Contract struct {
	empId    int
	basicPay int
}

// 实现了接口中计算工资方法
func (p Permanent) CalculateSalary() int {
	return p.basicPay + p.pf
}

// 实现了接口中计算工资方法
func (c Contract) CalculateSalary() int {
	return c.basicPay
}

// 计算工资总支出
// 函数参数类型是 SalaryCalculator 接口类型的切片
func totalExpense(s []SalaryCalculator) {
	expense := 0
	for _, v := range s {
		// 会调用各自的CalculateSalary()实现
		// 即使多了一种员工类型，只要实现了接口中的方法，就无需修改此函数
		expense = expense + v.CalculateSalary()
	}
	fmt.Printf("Total Expense Per Month $%d", expense)
}

func TestInterface(t *testing.T) {
	// 声明了2个Permanent的变量pemp1、pemp2
	pemp1 := Permanent{1, 5000, 200}
	pemp2 := Permanent{2, 6000, 100}

	// 声明了1个Contact的变量cemp1
	cemp1 := Contract{3, 3000}

	// 声明一个包含 Permanent 和 Contact类型的 SalaryCalculator接口切片
	employees := []SalaryCalculator{pemp1, pemp2, cemp1}
	totalExpense(employees)
}
