package tempconv

import (
	"fmt"
	"testing"
)

func TestOne(t *testing.T) {
	fmt.Printf("%g\n", BoilingC-FreezingC)
	boilingF := CToF(BoilingC)
	fmt.Printf("%g\n", boilingF-CToF(FreezingC))
	// fmt.Printf("%g\n", boilingF-FreezingC)
}

func TestTwo(t *testing.T) {
	var c Celsius
	var f Fahrenheit
	fmt.Println(c == 0)
	fmt.Println(f >= 0)
	// fmt.Println(c == f) // 编译错误，类型不同
	fmt.Println(c == Celsius(f)) // 类型需要显示转换 T(v)
}

// 类型声明String 方法，在变量通过fmt包作为字符串输出时，可以控制类型值的显示方式
func (c Celsius) String() string { return fmt.Sprintf("%g°C of redefine", c) }

func TestThree(t *testing.T) {
	c := FToC(212.0)
	fmt.Println(c.String())
	fmt.Printf("%v\n", c) // 不需要显示调用字符串
	fmt.Printf("%s\n", c)
	fmt.Println(c)

	fmt.Printf("%g\n", c)
	fmt.Println(float64(c))
}
