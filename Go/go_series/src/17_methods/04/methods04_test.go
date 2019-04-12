package methodstest04

import (
	"fmt"
	"testing"
)

// 匿名字段的方法
// 属于结构体的匿名字段的方法可以被直接调用，就好像这些方法是属于定义了匿名字段的结构体一样。
type address struct {
	city  string
	state string
}

func (a address) fullAddress() {
	fmt.Printf("Full address: %s %s\n", a.city, a.state)
}

type person struct {
	firstName string
	lastName  string
	address   // 结构体类型的匿名字段
}

func TestAnonymousField(t *testing.T) {
	p := person{
		firstName: "Elon",
		lastName:  "Musk",
		address: address{
			city:  "Los Angeles",
			state: "California",
		},
	}
	// 访问 address 结构体的 fullAddress 方法
	// 明确的调用 p.address.fullAddress() 是没有必要的
	p.fullAddress()
	//p.address.fullAddress()
}
