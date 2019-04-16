package panic06

import (
	"fmt"
	"runtime/debug"
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
		debug.PrintStack()
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
