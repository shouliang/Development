package testing

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

// 单元测试
func TestSquare(t *testing.T) {
	inputs := [...]int{1, 2, 3}
	expected := [...]int{1, 4, 9}

	for i := 0; i < len(inputs); i++ {
		ret := square(inputs[i])
		if ret != expected[i] {
			t.Errorf("input is %d, the expected is %d, the actual %d", inputs[i], expected[i], ret)
		}
	}
}

func TestErrorInCode(t *testing.T) {
	fmt.Println("Start")
	t.Error("Error")
	fmt.Println("End")
}

func TestFailInCode(t *testing.T) {
	fmt.Println("Start")
	t.Fatal("Error") // exit
	fmt.Println("End")
}

// go test -v cover

// 断言
// go get -u github.com/stretchr/testify/assert
// 单元测试
func TestSquareWithAssert(t *testing.T) {
	inputs := [...]int{1, 2, 3}
	expected := [...]int{1, 5, 9}

	for i := 0; i < len(inputs); i++ {
		ret := square(inputs[i])
		assert.Equal(t, expected[i], ret)
	}
}
