package interface04

import (
	"fmt"
	"testing"
)

type Describer interface {
	Describe()
}

type Person struct {
	name string
	age  int
}

func (p Person) Describe() {
	fmt.Printf("%s is %d years old\n", p.name, p.age)
}

// 还可以将一个类型和接口相比较。如果一个类型实现了接口，
// 那么该类型与其实现的接口就可以互相比较。
func TestCompareToInterface(t *testing.T) {
	findType("Steven")
	p := Person{
		name: "zhangsan",
		age:  27,
	}
	findType(p)
}

// 还可以将一个类型和接口相比较。如果一个类型实现了接口，
// 那么该类型与其实现的接口就可以互相比较。
func findType(i interface{}) {
	switch v := i.(type) {
	case Describer:
		v.Describe()
	default:
		fmt.Printf("Unkown type\n")
	}
}
