// 组合取代继承,通过嵌套结构体进行组合
package main

import "fmt"

// 作者
type author struct {
	firstName string
	lastName  string
	bio       string
}

func (a author) fullName() string {
	return fmt.Sprintf("%s %s", a.firstName, a.lastName)
}

// 博客： 嵌套了作者author，可以直接使用其字段和方法，类似于继承
type post struct {
	title   string
	content string
	author
}

func (p post) details() {
	fmt.Println("Title: ", p.title)
	fmt.Println("Content: ", p.content)

	// 一旦结构体内嵌套了一个结构体字段，Go 可以使我们访问其嵌套的字段，
	// 好像这些字段属于外部结构体一样
	// fmt.Println("Author: ", p.author.fullName())
	// fmt.Println("Bio: ", p.author.bio)

	fmt.Println("Author: ", p.fullName())
	fmt.Println("Bio: ", p.bio)
}

// post 可以自定义 fullName() 这样就会覆盖掉嵌套类中的方法
// func (p post) fullName() string {
// 	return "just post fullName"
// }

// 结构体切片的嵌套
type website struct {
	// 错误的原因是结构体不能嵌套一个匿名切片。我们需要一个字段名
	// []post
	posts []post
}

func (w website) contents() {
	fmt.Printf("Contents of Website\n")
	for _, v := range w.posts {
		v.details()
		fmt.Println()
	}
}

func main() {
	author1 := author{
		"Naveen",
		"Ramanathan",
		"Golang Enthusiast",
	}

	post1 := post{
		"Inheritance in Go",
		"Go supports composition instead of inheritance",
		author1,
	}

	post2 := post{
		"Struct instead of Classes in Go",
		"Go does not support classes but methods can be added to structs",
		author1,
	}
	post3 := post{
		"Concurrency",
		"Go is a concurrent language and not a parallel one",
		author1,
	}

	// post1.details()

	w := website{
		posts: []post{post1, post2, post3},
	}
	w.contents()

}
