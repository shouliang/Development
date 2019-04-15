/*
什么是 panic？
在 Go 语言中，程序中一般是使用错误来处理异常情况。对于程序中出现的大部分异常情况，错误就已经够用了。

但在有些情况，当程序发生异常时，无法继续运行。在这种情况下，我们会使用 panic 来终止程序。
当函数发生 panic 时，它会终止运行，在执行完所有的延迟函数后，程序控制返回到该函数的调用方。
这样的过程会一直持续下去，直到当前协程的所有函数都返回退出，然后程序会打印出 panic 信息，接着打印出堆栈跟踪（Stack Trace），
最后程序终止
*/

/*
什么时候应该使用 panic？
需要注意的是，你应该尽可能地使用错误，而不是使用 panic 和 recover。只有当程序不能继续运行的时候，
才应该使用 panic 和 recover 机制。

panic 有两个合理的用例。

发生了一个不能恢复的错误，此时程序不能继续运行。 一个例子就是 web 服务器无法绑定所要求的端口。
在这种情况下，就应该使用 panic，因为如果不能绑定端口，啥也做不了。

发生了一个编程上的错误。 假如我们有一个接收指针参数的方法，而其他人使用 nil 作为参数调用了它。
在这种情况下，我们可以使用 panic，因为这是一个编程错误：用 nil 参数调用了一个只能接收合法指针的方法。
*/
package panic01

import (
	"fmt"
	"testing"
)

func fullName(firstName *string, lastName *string) {
	if firstName == nil {
		panic("runtime error: first name cannot be nil")
	}
	if lastName == nil {
		panic("runtime error: last name cannot be nil")
	}

	// 发生panic，后续语句不会执行到
	fmt.Printf("%s %s\n", *firstName, *lastName)
	fmt.Println("returned normally from fullName")
}

func TestPanic(t *testing.T) {
	firstName := "Elon"
	fullName(&firstName, nil)
	fmt.Println("returned normally from main")
}
