// panic 用于不可恢复的错误
// panic 退出前会执行defer指定的内容，会输出当前调用栈的信息

// os.Exit 退出时不会调用defer指定的函数，不输出当前调用栈的信息
package panic_recover

import (
	"errors"
	"fmt"
	"testing"
)

func TestPanicVxExit(t *testing.T) {
	// defer func() {
	// 	fmt.Println("Finally")
	// }()

	defer func() {
		if err := recover(); err != nil { // recover接收从panic传递出来的error,进行恢复处理，故程序运行正常，没有抛出错误调用栈
			fmt.Println("recovered from", err) // 不处理，容易造成僵尸进程，倒不如让你crash, "let it crash",守护进程会重启来发现错误
		}
	}()

	fmt.Println("start")

	panic(errors.New("Something wrong"))
	//os.Exit(-1)

	//fmt.Println("End")
}
