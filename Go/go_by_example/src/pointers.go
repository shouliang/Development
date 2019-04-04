// 指针
package main

import "fmt"

// go语言函数参数都是值传递，会copy一份，此处copy的是值
// 故在此值上所做的改变不会影响到原来的值
func zeroval(ival int) {
	ival = 0
}

// go语言函数参数都是值传递，会copy一份，此处copy的是指针
// 即多了一份指向原来的指针，故在此指针上所做的改变也会影响到原来的的值
func zeroptr(iptr *int) {
	*iptr = 0
}

func main() {
	i := 1
	fmt.Println("initial:", i)

	zeroval(i)
	fmt.Println("zeroval:", i)

	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	fmt.Println("pointer:", &i)
}
