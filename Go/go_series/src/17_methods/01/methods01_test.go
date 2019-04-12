package methodstest01

import (
	"fmt"
	"math"
	"testing"
)

/* 什么是方法
方法其实就是一个函数，在 func 这个关键字和方法名中间加入了一个特殊的接收器类型。
接收器可以是结构体类型或者是非结构体类型。接收器是可以在方法的内部访问的。
下面就是创建一个方法的语法。
func (t Type) methodName(parameter list) {
}
*/

type Employee struct {
	name     string
	salary   int
	currency string
}

//  displaySalary() 方法将 Employee 做为接收器类型
func (e Employee) displaySalary() {
	fmt.Printf("Salary of %s is %s%d\n", e.name, e.currency, e.salary)
}

// displaySalary()函数，把 Employee 当做参数传入
func displaySalary(e Employee) {
	fmt.Printf("Salary of %s is %s%d\n", e.name, e.currency, e.salary)
}

// 方法示例
func TestMethods(t *testing.T) {
	emp1 := Employee{
		name:     "Sam Adolf",
		salary:   5000,
		currency: "$",
	}

	//调用 Employee 类型的 displaySalary() 方法
	emp1.displaySalary()

	// 把 Employee 当做参数传入函数
	displaySalary(emp1)
}

/* 为什么我们已经有函数了还需要方法呢？
Go 不是纯粹的面向对象编程语言，而且Go不支持类。因此，基于类型的方法是一种实现和类相似行为的途径。
相同的名字的方法可以定义在不同的类型上，而相同名字的函数是不被允许的。
假设我们有一个 Square 和 Circle 结构体。
可以在 Square 和 Circle 上分别定义一个 Area 方法。见下面的程序。
*/
type Rectangle struct {
	length int
	width  int
}

type Circle struct {
	radius float64
}

func (r Rectangle) Area() int {
	return r.length * r.width
}

func (c Circle) Area() float64 {
	return math.Pi * c.radius * c.radius
}

func TestWhyHavingMethods(t *testing.T) {
	r := Rectangle{
		length: 10,
		width:  5,
	}
	t.Logf("Area of rectangle %d\n", r.Area())

	c := Circle{
		radius: 10,
	}
	t.Logf("Area of circle %f", c.Area())
}
