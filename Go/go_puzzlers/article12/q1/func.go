package main

import (
	"errors"
	"fmt"
)

// 自定义函数类型operate
type operate func(x, y int) int

// 函数类型operate作为另外一个函数的参数
func calculate(x int, y int, op operate) (int, error) {
	if op == nil {
		return 0, errors.New("invalid operation")
	}

	return op(x, y), nil
}

type calculateFunc func(x int, y int) (int, error)

// 函数类型作为另外一个函数的返回值
func genCalculator(op operate) calculateFunc {
	return func(x int, y int) (int, error) {
		if op == nil {
			return 0, errors.New("invalid operation")
		}
		return op(x, y), nil
	}
}

func main() {
	x, y := 12, 23
	op := func(x, y int) int {
		return x + y
	}
	result, err := calculate(x, y, op)
	fmt.Printf("The result: %d (error: %v)\n", result, err)

	x, y = 56, 78
	add := genCalculator(op)
	result, err = add(x, y)
	fmt.Printf("The result: %d (error: %v)\n", result, err)
}
