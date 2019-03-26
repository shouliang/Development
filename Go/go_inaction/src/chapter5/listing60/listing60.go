// 展示当内部类型和外部类型要实现同一个接口的做法
package main

import "fmt"

type notifier interface {
	notify()
}

type user struct {
	name  string
	email string
}

// user类型实现了接口
func (u *user) notify() {
	fmt.Printf("Sending user email to %s<%s>\n", u.name, u.email)
}

// 定义admin类型，嵌入了user类型，类似于继承了user类型的方法
type admin struct {
	user
	level string
}

// 为admin类型增加了notifier接口的实现
func (a *admin) notify() {
	fmt.Printf("Sending admin email to %s<%s>\n", a.name, a.email)
}

func main() {
	ad := admin{
		user: user{
			name:  "john smith",
			email: "john@yahoo.com",
		},
		level: "super",
	}

	ad.user.notify()

	// 调用自己的实现，不会被内部类型的方法提升，类似于覆盖了父类的方法
	ad.notify()

}

func sendNotification(n notifier) {
	n.notify()
}
