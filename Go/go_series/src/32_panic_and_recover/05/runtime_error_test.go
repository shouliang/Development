/*
运行时 panic
运行时错误（如数组越界）也会导致 panic。这等价于调用了内置函数 panic，
其参数由接口类型 runtime.Error 给出。runtime.Error 接口的定义如下：

type Error interface {
    error
    // RuntimeError is a no-op function but
    // serves to distinguish types that are run time
    // errors from ordinary errors: a type is a
    // run time error if it has a RuntimeError method.
    RuntimeError()
}
而 runtime.Error 接口满足内建接口类型 error。
*/
package panic05

import (
	"fmt"
	"testing"
)

func r() {
	if r := recover(); r != nil {
		fmt.Println("Recovered", r)
	}
}

func a() {
	defer r()
	n := []int{5, 7, 4}
	fmt.Println(n[3])
	fmt.Println("normally returned from a")
}

func TestRecover(t *testing.T) {
	a()
	fmt.Println("normally returned from main")
}
