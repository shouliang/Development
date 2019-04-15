package main

import "26_structsAndClasses/oop/employee"

// go install 26_structsAndClasses/oop 依次查找所有GOPATH中的目录寻找oop包和它依赖的包
func main() {
	// e := employee.Employee{
	// 	FirstName:   "Sam",
	// 	LastName:    "Adolf",
	// 	TotalLeaves: 30,
	// 	LeavesTaken: 20,
	// }
	// e.LeavesRemaining()

	// 使用 Employee 创建的零值变量没有什么用。它没有合法的姓名，也没有合理的休假细节。
	// e1 := employee.Employee{}
	// e1.LeavesRemaining()

	// 现在创建 employee 变量的唯一方法就是使用 New 函数
	e := employee.New("Sam", "Adolf", 30, 20)
	e.LeavesRemaining()
}
