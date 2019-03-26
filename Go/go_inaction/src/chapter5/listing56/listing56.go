// 展示如何将嵌入类型应用于接口
package main

import "fmt"

// 定义接口
type notifer interface {
	notify()
}

// 定义user类型
type user struct {
	name  string
	email string
}

// 定义方法，方法的接收者为user类型的指针
func (u *user) notify() {
	fmt.Printf("Sending user email to %s<%s>\n", u.name, u.email)
}

// 定义admin类型
type admin struct {
	user  // 嵌入类型或内部类型
	level string
}

func main() {
	ad := admin{
		user: user{
			name:  "john smith",
			email: "john@yahoo.com",
		},
		level: "super",
	}

	// admin 并没有实现该接口
	// 用于实现接口的内部类型的方法，被提升到外部类型
	// 类似于外部类型继承了内部类型的方法
	sendNotification(&ad)

}

func sendNotification(n notifer) {
	n.notify()
}
