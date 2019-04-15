/*
发生 panic 时的 defer
我们重新总结一下 panic 做了什么。当函数发生 panic 时，它会终止运行，在执行完所有的延迟函数后，
程序控制返回到该函数的调用方。这样的过程会一直持续下去，直到当前协程的所有函数都返回退出，
然后程序会打印出 panic 信息，接着打印出堆栈跟踪，最后程序终止。

如果有延迟函数，会先调用它，然后程序控制返回到函数调用方。
*/
package panic02

import (
	"fmt"
	"testing"
)

// 首先执行 fullName 函数中的 defer 语句。程序打印出： deferred call in fullName
// 接着程序返回到 main 函数，执行了 main 函数的延迟调用，因此会输出：deferred call in main
func fullName(firstName *string, lastName *string) {
	defer fmt.Println("deferred call in fullName")
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
	defer fmt.Println("defer call in main")
	firstName := "Elon"
	fullName(&firstName, nil)
	fmt.Println("returned normally from main")
}
