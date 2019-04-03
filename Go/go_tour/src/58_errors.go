// 错误
/*
	Go程序中使用 error 值来表示错误状态
	与 fmt.Stringer类似， error类型也是一个内建接口：
	type error interface {
		Error() string
	}


	通常函数会返回一个error值，调用它的代码应当判断这个错误是否等于nil,error为nil表示成功，非nil表示有错误
*/

package main

import (
	"fmt"
	"time"
)

type MyError struct {
	When time.Time
	What string
}

// MyError 实现了error接口中的 Error()方法,返回类型为string
func (e *MyError) Error() string {
	return fmt.Sprintf("at %v, %s",
		e.When, e.What)
}

// run 函数的返回类型为error, return语句返回为*MyError类型，因为*MyError实现了接口error中的Error()方法
func run() error {
	return &MyError{
		time.Now(),
		"it didn't work",
	}

}

func main() {
	if err := run(); err != nil {
		fmt.Println(err)
	}
}
