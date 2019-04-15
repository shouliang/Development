/*
recover
recover 是一个内建函数，用于重新获得 panic 协程的控制。

recover 函数的标签如下所示：

func recover() interface{}
只有在延迟函数的内部，调用 recover 才有用。在延迟函数内调用 recover，可以取到 panic 的错误信息，
并且停止 panic 续发事件（Panicking Sequence），程序运行恢复正常。
如果在延迟函数的外部调用 recover，就不能停止 panic 续发事件。
*/
package panic03

import (
	"fmt"
	"testing"
)

func recoverName() {
	if r := recover(); r != nil {
		fmt.Println("recovered from", r)
	}
}

func fullName(firstName *string, lastName *string) {
	defer recoverName()
	if firstName == nil {
		panic("runtime error: first name cannot be nil")
	}
	if lastName == nil {
		panic("runtime error: last name cannot be nil")
	}

	fmt.Printf("%s %s\n", *firstName, *lastName)
	fmt.Println("returned normally from fullName")
}

func TestPanic(t *testing.T) {
	defer fmt.Println("defer call in main")
	firstName := "Elon"
	fullName(&firstName, nil)
	fmt.Println("returned normally from main")
}
