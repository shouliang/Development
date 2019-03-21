package goroutine_test

import (
	"fmt"
	"testing"
)

func TestGoRoutine(t *testing.T) {
	for i := 0; i < 10; i++ {
		go func() {
			fmt.Println(i)
		}()
	}
}
