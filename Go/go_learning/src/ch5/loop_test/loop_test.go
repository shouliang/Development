// 遍历
package loop_test

import "testing"

func TestWhileLoop(t *testing.T) {
	n := 0
	// 此处for 相当于 while,但是go语言中无while,用for可以表示while
	for n < 5 {
		t.Log(n)
		n++
	}
}
