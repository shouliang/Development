package equal

import (
	"fmt"
	"testing"
)

func TestEqual(t *testing.T) {
	fmt.Println(Equal([]int{1, 2, 3}, []int{1, 2, 3}))
	fmt.Println(Equal([]string{"foo"}, []string{"bar"}))
	fmt.Println(Equal([]string(nil), []string{}))
	fmt.Println(Equal(map[string]int(nil), map[string]int{}))
}

func TestEqualCycle(t *testing.T) {
	type link struct {
		value string
		tail  *link
	}

	a, b, c := &link{value: "a"}, &link{value: "b"}, &link{value: "c"}
	a.tail, b.tail, c.tail = b, a, c
	fmt.Println(Equal(a, a))
	fmt.Println(Equal(b, b))
	fmt.Println(Equal(c, c))
	fmt.Println(Equal(a, b))
	fmt.Println(Equal(a, c))
	fmt.Println(Equal(b, c))
}

func Test(t *testing.T) {
	one, oneAgain, two := 1, 1, 2

	type CyclePtr *CyclePtr
	var cyclePtr1, cyclePtr2 CyclePtr
	cyclePtr1 = &cyclePtr1
	cyclePtr2 = &cyclePtr2

	type CycleSlice []CycleSlice
	var cycleSlice = make(CycleSlice, 1)
	cycleSlice[0] = cycleSlice

	ch1, ch2 := make(chan int), make(chan int)
	var ch1ro <-chan int = ch1

	type mystring string

	var iface1, iface1Again, iface2 interface{} = &one, &oneAgain, &two

	for _, test := range []struct {
		x, y interface{}
		want bool
	}{
		{1, 1, true},
		{1, 2, false},
		{1, 1.0, false},
		{"foo", "foo", true},
		{"foo", "bar", false},
		{mystring("foo"), "foo", false},

		// channels
		{ch1, ch1, true},
		{ch1, ch2, false},
		{ch1ro, ch1, false},

		/// interfaces
		{&iface1, &iface1, true},
		{&iface1, &iface2, false},
		{&iface1Again, &iface1, true},
	} {
		if Equal(test.x, test.y) != test.want {
			t.Errorf("Equal(%v %v) = %t", test.x, test.y, !test.want)
		}
	}
}
