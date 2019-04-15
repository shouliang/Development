/*什么是 defer？
defer 语句的用途是：含有 defer 语句的函数，会在该函数将要返回之前，调用另一个函数
*/
package defertest01

import (
	"fmt"
	"testing"
)

func finished() {
	fmt.Println("Finished finding largest")
}

func largest(nums []int) {
	defer finished()

	fmt.Println("Started finding largest")
	max := nums[0]
	for _, v := range nums {
		if v > max {
			max = v
		}
	}

	fmt.Println("Largest number in", nums, "is", max)
}

// defer 语句的用途是：含有 defer 语句的函数，会在该函数将要返回之前，调用另一个函数
func TestDeferInFunction(t *testing.T) {
	nums := []int{78, 109, 2, 563, 300}
	largest(nums)
}

type person struct {
	firstName string
	lastName  string
}

func (p person) fullName() {
	fmt.Printf("%s %s", p.firstName, p.lastName)
}

// defer 不仅限于函数的调用，调用方法也是合法的
func TestDeferInMethod(t *testing.T) {
	p := person{
		firstName: "John",
		lastName:  "Smith",
	}
	defer p.fullName()
	fmt.Printf("Welcom ")
}

/*实参取值（Arguments Evaluation）
在 Go 语言中，并非在调用延迟函数的时候才确定实参，
而是当执行 defer 语句的时候，就会对延迟函数的实参进行求值。
*/
func printA(a int) {
	fmt.Println("value of a in deferred function", a)
}

func TestArgumentsEvaluation(t *testing.T) {
	a := 5
	defer printA(a) //由于 a 等于 5，因此延迟函数 printA 的实参也等于 5
	a = 10
	// defer printA(a)
	fmt.Println("value of a before deferred function call", a)
}

/*defer 栈
当一个函数内多次调用 defer 时，Go 会把 defer 调用放入到一个栈中，随后按照后进先出（Last In First Out, LIFO）的顺序执行。
*/
func TestDeferStack(t *testing.T) {
	name := "zhangsan"
	t.Log("Orignal String:", name)
	t.Logf("Reversed String:")
	for _, v := range []rune(name) {
		defer t.Logf("%c", v)
	}
}
