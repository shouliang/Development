package error_test

import (
	"errors"
	"fmt"
	"testing"
)

var LessThanTwoError = errors.New("n should be not less than 2") // errors.New生成error的一个实例
var LargerThanHundredError = errors.New("n should be not larger than 100")

func GetFibonacci(n int) ([]int, error) {
	if n < 2 {
		return nil, LessThanTwoError
	}

	if n > 100 {
		return nil, LargerThanHundredError
	}

	fibList := []int{1, 1}

	for i := 2; i < n; i++ {
		fibList = append(fibList, fibList[i-2]+fibList[i-1])
	}

	return fibList, nil
}

func TestGetFibnacci(t *testing.T) {
	// n := 10
	n := 1
	// n := 101
	if v, err := GetFibonacci(n); err != nil { // 判断err!=nil，及早失败，避免嵌套过深，所有的错误都没有后，才正确输出
		if err == LessThanTwoError {
			fmt.Println("It is less.")
		}
		if err == LargerThanHundredError {
			fmt.Println("It is large.")
		}
		t.Error(err)
	} else {
		t.Log(v)
	}

}
