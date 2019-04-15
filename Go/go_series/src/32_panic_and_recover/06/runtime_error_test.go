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

		/*恢复后获得堆栈跟踪
		当我们恢复 panic 时，我们就释放了它的堆栈跟踪。
		实际上，在上述程序里，恢复 panic 之后，我们就失去了堆栈跟踪。
		有办法可以打印出堆栈跟踪，就是使用 Debug 包中的 PrintStack 函数。
		*/
		// debug.PrintStack()
	}
}

func a() {
	defer r() // 恢复了panic，所以不会打印堆栈信息
	n := []int{5, 7, 4}
	fmt.Println(n[3])
	fmt.Println("normally returned from a")
}

func TestRecover(t *testing.T) {
	a()
	fmt.Println("normally returned from main")
}
