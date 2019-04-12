package interfaceII01

// 个人理解就是使用指针接受者的方法，若该方法是接口中的方法，就不能使用值类型接受者调用，而必须使用指针类型的接受者调用才可以
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

// 值类型接受者实现接口中的方法，值类型和指针类型接受者均可
func (p Person) Describe() {
	fmt.Printf("%s is %d years old\n", p.name, p.age)
}

type Address struct {
	state   string
	country string
}

// 指针类型接受者实现接口中的方法，只能接受指针类型的接受者
func (a *Address) Describe() {
	fmt.Printf("State %s Country %s", a.state, a.country)
}

func TestValueReceiverAndPointerReceiver(t *testing.T) {
	var d1 Describer
	p1 := Person{"Sam", 25}

	d1 = p1
	d1.Describe()

	d1 = &p1
	d1.Describe()

	var d2 Describer
	a := Address{"Washington", "USA"}

	// 对于使用指针接受者的方法，用一个指针来调用都是合法的。
	// 但接口中存储的具体值（Concrete Value）并不能取到地址
	// cannot use a (type Address) as type Describer in assignment:
	// Address does not implement Describer (Describe method has pointer receiver)
	// d2 = a
	// d2.Describe()

	d2 = &a
	d2.Describe()

}
