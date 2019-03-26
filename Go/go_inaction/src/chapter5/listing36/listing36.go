// 展示了如何使用接口
package main

import "fmt"

// 定义接口
type notifier interface {
	notify()
}

type user struct {
	name  string
	email string
}

// 使用指针类型接收者来实现一个接口，只有指向那个类型的指针才能实现对应的接口
func (u *user) notify() {
	fmt.Printf("Sending user email to %s<%s>\n", u.name, u.email)
}

func main() {
	u := user{"Bill", "bill@gmail.com"}

	// cannot use u (type user) as type notifier in argument to sendNotification:
	// user does not implement notifier (notify method has pointer receiver)
	// sendNotification(u)

	// 使用指针类型接收者来实现一个接口，只有指向那个类型的指针才能实现对应的接口
	sendNotification(&u)
}

func sendNotification(n notifier) {
	n.notify()
}
