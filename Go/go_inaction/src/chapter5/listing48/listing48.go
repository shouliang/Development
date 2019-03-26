// 使用接口展示多态行为
package main

import "fmt"

// 定义接口
type notifier interface {
	notify()
}

// 定义user类型
type user struct {
	name  string
	email string
}

// user指针类型实现了接口：不用显式声明继承，只要实现了接口中的全部方法即可
func (u *user) notify() {
	fmt.Printf("Sending user email to %s<%s>\n", u.name, u.email)
}

// 定义admin类型
type admin struct {
	name  string
	email string
}

// amdin指针类型实现了接口
func (a *admin) notify() {
	fmt.Printf("Sending admin email to %s<%s>\n", a.name, a.email)
}

func main() {
	// 创建一个user类型并传给sendNotification
	bill := user{"Bill", "bill@gmail.com"}
	sendNotification(&bill)

	// 创建一个admin类型并传给sendNotification
	lisa := admin{"Lisa", "lisa@gmail.com"}
	sendNotification(&lisa)
}

// 多态，这个函数执行任何实现了它接口的行为
func sendNotification(n notifier) {
	n.notify()
}
