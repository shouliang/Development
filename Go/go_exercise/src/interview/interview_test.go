package interview

import (
	"fmt"
	"runtime"
	"sync"
	"testing"
)

func TestDeferCall(t *testing.T) {
	defer func() { t.Log("打印前") }()
	defer func() { t.Log("打印中") }()
	defer func() { t.Log("打印后") }()

	panic("触发异常")
}

type student struct {
	Name string
	Age  int
}

func TestParseStudent(t *testing.T) {
	m := make(map[string]*student)
	stus := []student{
		{Name: "zhou", Age: 24},
		{Name: "li", Age: 23},
		{Name: "wang", Age: 22},
	}
	for _, stu := range stus {
		m[stu.Name] = &stu
	}

	for _, stu := range stus {
		t.Log(stu)
	}
}

// 第一个go func中i是外部for的一个变量，地址不变化。遍历完成后，最终i=10。 故go func执行时，i的值始终是10。
// 第二个go func中i是函数参数，与外部for中的i完全是两个变量。 尾部(i)将发生值拷贝，go func内部指向值拷贝地址。
func TestGoroutine(t *testing.T) {
	runtime.GOMAXPROCS(1)
	wg := sync.WaitGroup{}
	wg.Add(20)
	for i := 0; i < 10; i++ {
		go func() {
			fmt.Println("A: ", i)
			wg.Done()
		}()
	}
	for i := 0; i < 10; i++ {
		go func(i int) {
			fmt.Println("B: ", i)
			wg.Done()
		}(i)
	}
	wg.Wait()
}

type People struct{}

func (p *People) ShowA() {
	fmt.Println("showA")
	p.ShowB()
}
func (p *People) ShowB() {
	fmt.Println("showB")
}

type Teacher struct {
	People
}

func (t *Teacher) ShowB() {
	fmt.Println("teacher showB")
}

func TestOOP(t *testing.T) {
	teacher := Teacher{}
	teacher.ShowA()
}

func TestSelect(t *testing.T) {
	runtime.GOMAXPROCS(1)
	intChan := make(chan int, 1)
	stringChan := make(chan string, 1)
	intChan <- 1
	stringChan <- "hello"
	select {
	case value := <-intChan:
		t.Log(value)
	case value := <-stringChan:
		panic(value)
	}
}

func calc(index string, a, b int) int {
	ret := a + b
	fmt.Println(index, a, b, ret)
	return ret
}

func TestDefer(t *testing.T) {
	a := 1
	b := 2
	defer calc("1", a, calc("10", a, b))
	a = 0
	defer calc("2", a, calc("20", a, b))
	b = 1
}

func TestAppend(t *testing.T) {
	s := make([]int, 5)
	s = append(s, 1, 2, 3)
	t.Log(s)

	s1 := make([]int, 0)
	s1 = append(s1, 1, 2, 3)
	t.Log(s1)
}

type Person interface {
	Speak(string) string
}

type Stduent struct{}

func (stu *Stduent) Speak(think string) (talk string) {
	if think == "bitch" {
		talk = "You are a good boy"
	} else {
		talk = "hi"
	}
	return
}

func TestMethod(t *testing.T) {
	// var per Person = Stduent{}
	var per Person = &Stduent{}
	think := "bitch"
	fmt.Println(per.Speak(think))
}
