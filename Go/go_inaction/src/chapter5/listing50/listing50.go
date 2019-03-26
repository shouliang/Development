// 展示了如何将一个类型嵌入另外一个类型，
// 以及内部类型和外部类型之间的关系
package main

import "fmt"

// 自定义user类型
type user struct {
	name  string
	email string
}

// 定义一个方法，接收者为user的指针类型
func (u *user) notify() {
	fmt.Printf("Sending user email to %s<%s>\n", u.name, u.email)
}

// 自定义admin类型
type admin struct {
	user  // 嵌入类型，只需要声明这个类型的名字即可
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
	// 可以直接访问内部类型的方法
	ad.user.notify()

	// 内部类型的方法也被提升到外部类型
	// 即外部类型拥有了内部类型的方法，类似于外部类型继承了内部类型
	ad.notify()
}
