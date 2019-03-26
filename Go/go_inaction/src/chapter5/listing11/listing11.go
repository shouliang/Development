// 展示了如何声明并使用方法
package main

import "fmt"

// 自定义user类型
type user struct {
	name  string
	email string
}

// 值接收者实现了一个方法
func (u user) notify() {
	fmt.Printf("Sending User Email To %s<%s>\n", u.name, u.email)
}

// 指针接收者实现了一个方法
func (u *user) changeEmail(email string) {
	u.email = email
}

func main() {
	// user类型的值 调用使用 值接收者 声明的方法
	bill := user{"Bill", "bill@gmail.com"}
	bill.notify()

	// user类型的指针 也可以调用使用 值接收者 声明的方法
	lisa := &user{"Lisa", "lisa@gmail.com"}
	lisa.notify()

	// user类型的值 也可以调用使用 指针接收者 声明的方法
	bill.changeEmail("bill@163.com")
	bill.notify()

	// user类型的指针 调用使用 指针接收者 声明的方法
	lisa.changeEmail("lisa@163.com")
	lisa.notify()
}
