package methodstest03

import (
	"fmt"
	"testing"
)

type rectangle struct {
	length int
	width  int
}

// 方法中使用值接收器 : 计算面积
func (r rectangle) area() {
	fmt.Printf("Area Method result: %d\n", r.length*r.width)
}

// 函数中使用值接收器 : 计算面积
func area(r rectangle) {
	fmt.Printf("Area Method result: %d\n", r.length*r.width)
}

// 方法中使用指针接收器：计算周长
func (r *rectangle) perimeter() {
	fmt.Println("perimeter method output:", 2*(r.length+r.width))
}

// 函数中使用指针接收器：计算周长
func perimeter(r *rectangle) {
	fmt.Println("perimeter method output:", 2*(r.length+r.width))
}

func TestValueReceiversAndPointerReceivers(t *testing.T) {
	r := rectangle{
		length: 10,
		width:  5,
	}

	// 指针类型
	pr := &r

	// 方法调用
	// 不管定义方法时的接收者是值类型还是指针类型
	// 方法调用时可以是值类型也可以是指针类型
	r.area()
	pr.area()

	r.perimeter()
	pr.perimeter()

	// 函数调用
	area(r)
	// 值类型的参数不能传入指针类型的参数，否则会编译错误
	//area(pr)

	// 指针类型的参数不能传入值类型的参数，否则会编译错误
	//perimeter(r)
	perimeter(pr)

}
