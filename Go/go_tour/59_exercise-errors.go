package main

import (
	"fmt"
	"math"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("cannot Sqrt negative number:%v", float64(e))
}

func Sqrt(x float64) (float64, error) {
	if x < 0 {
		return 0, ErrNegativeSqrt(x) // 将x转换成ErrNegativeSqrt，而ErrNegativeSqrt实现了接口error中的Error()方法，返回字符串
	} else {
		return math.Sqrt(x), nil
	}

}

func main() {
	num := float64(-2)
	//num := float64(2)
	if v, error := Sqrt(num); error != nil {
		fmt.Println(error)
	} else {
		fmt.Println(v)
	}

}
