package func_test

import (
	"fmt"
	"math/rand"
	"testing"
	"time"
)

// 多返回值
func returnMultiValues() (int, int) {
	return rand.Intn(10), rand.Intn(20)
}

func timeSpent(inner func(op int) int) func(op int) int {
	return func(n int) int {
		start := time.Now()
		ret := inner(n)

		fmt.Println("time spent:", time.Since(start).Seconds())
		return ret
	}
}

func slowFun(op int) int {
	time.Sleep(time.Second * 1)
	return op
}

// 可变长参数: 不需要指定参数个数，但是参数类型要求一致,实质会转换成数组，通过数组遍历来完成
func Sum(ops ...int) int {
	s := 0
	for _, op := range ops {
		s += op
	}
	return s
}

func TestFn(t *testing.T) {
	a, b := returnMultiValues()
	t.Log(a, b)

	tsSF := timeSpent(slowFun)
	t.Log(tsSF(10))
}

func TestVarParam(t *testing.T) {
	// 可变长参数
	t.Log(Sum(1, 2, 3))
	t.Log(Sum(1, 2, 3, 4, 5))
}

func Clear() {
	fmt.Println("Clear resource.")
}

// defer 延迟执行，在函数返回前才会执行，依据这种特性 ，清理资源和释放锁
func TestDefer(t *testing.T) {
	defer Clear()
	fmt.Println("Start")

	// 即使panic，defer后面的语句依然会执行，但是普通语句在panic后不会执行
	panic("error")
    fmt.Println("never excute")
}
