package employee

import "fmt"

// Go 不支持类，但结构体能够很好地取代类，而以 New(parameters) 签名的方法可以替代构造器。

/*使用结构体，而非类
Go 不支持类，而是提供了结构体。结构体中可以添加方法。
这样可以将数据和操作数据的方法绑定在一起，实现与类相似的效果。
*/

// type Employee struct {
// 	FirstName   string
// 	LastName    string
// 	TotalLeaves int
// 	LeavesTaken int
// }

// func (e Employee) LeavesRemaining() {
// 	fmt.Printf("%s %s has %d leaves remaining\n", e.FirstName, e.LastName, (e.TotalLeaves - e.LeavesTaken))
// }

// 把 employee 结构体变为了不可引用的，防止其他包对它的访问
type employee struct {
	firstName   string
	lastName    string
	totalLeaves int
	leavesTaken int
}

// New(parameters) 签名的方法可以替代构造器
func New(firstName string, lastName string, totalLeave int, leavesTaken int) employee {
	e := employee{firstName, lastName, totalLeave, leavesTaken}
	return e
}

// 结构体中可以添加方法。
// 这样可以将数据和操作数据的方法绑定在一起，实现与类相似的效果。
// 计算和显示员工的剩余休假数
func (e employee) LeavesRemaining() {
	fmt.Printf("%s %s has %d leaves remaining\n", e.firstName, e.lastName, (e.totalLeaves - e.leavesTaken))
}
