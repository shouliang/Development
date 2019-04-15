/*
panic，recover 和 Go 协程
只有在相同的 Go 协程中调用 recover 才管用。recover 不能恢复一个不同协程的 panic。
*/
package panic04

import (
	"fmt"
	"testing"
	"time"
)

func recovery() {
	if r := recover(); r != nil {
		fmt.Println("recovered:", r)
	}
}

func a() {
	defer recovery() // 不能恢复另外一个协程b()中的panic
	fmt.Println("Inside A")
	go b()
	time.Sleep(1 * time.Second)
}

func b() {
	fmt.Println("Inside B")
	panic("oh, B panicked")
}

func TestRecover(t *testing.T) {
	a()
	fmt.Println("normally returned from main")
}
