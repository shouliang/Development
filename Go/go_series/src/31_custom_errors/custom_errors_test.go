package customeerrors

import (
	"errors"
	"fmt"
	"math"
	"testing"
)

/* 1.使用 New 函数创建自定义错误
创建自定义错误最简单的方法是使用 errors 包中的 New 函数。
*/
func circleArea01(radius float64) (float64, error) {
	if radius < 0 {
		return 0, errors.New("Area calculation failed,radius is less than zero")
	}
	return math.Pi * radius * radius, nil
}

/*2.使用 Errorf 给错误添加更多信息
上面的程序效果不错，但是如果我们能够打印出当前圆的半径，那就更好了。
这就要用到 fmt 包中的 Errorf 函数了。
Errorf 函数会根据格式说明符，规定错误的格式，并返回一个符合该错误的字符串。
*/
func circleArea02(radius float64) (float64, error) {
	if radius < 0 {
		return 0, fmt.Errorf("Area calculation failed, radius %0.2f is less than zero", radius)
	}
	return math.Pi * radius * radius, nil
}

func TestNew(t *testing.T) {
	radius := -23.0
	area, err := circleArea01(radius)
	if err != nil {
		t.Log(err)
		return
	}
	t.Logf("Area of circle %0.2f", area)
}

func TestErrorf(t *testing.T) {
	radius := -23.0
	area, err := circleArea02(radius)
	if err != nil {
		t.Log(err)
		return
	}
	t.Logf("Area of circle %0.2f", area)
}

/* 3.使用结构体类型和字段提供错误的更多信息
错误还可以用实现了 error 接口的结构体来表示。这种方式可以更加灵活地处理错误
*/
type areaError struct {
	err    string
	radius float64
}

// 实现 error 接口。
func (e *areaError) Error() string {
	return fmt.Sprintf("radius %0.2f: %s", e.radius, e.err)
}

func circleArea03(radius float64) (float64, error) {
	if radius < 0 {
		return 0, &areaError{"radius is negative", radius}
	}
	return math.Pi * radius * radius, nil
}

// 检查了错误是否为 nil，并断言了 *areaError 类型。
// 如果错误是 *areaError 类型，我们就可以用 err.radius 来获取错误的半径，打印出自定义错误的消息
func TestErrorUsingStruct(t *testing.T) {
	radius := -23.0
	area, err := circleArea03(radius)
	if err, ok := err.(*areaError); ok {
		t.Logf("Radius %0.2f is less than zero", err.radius)
		return
	}
	t.Logf("Area of circle %0.2f", area)
}

// 4.使用结构体类型的方法来提供错误的更多信息
type areaCustomError struct {
	err    string
	length float64
	width  float64
}

// 有了错误类型，我们来实现 error 接口，并给该错误类型添加两个方法，使它提供了更多的错误信息
func (e *areaCustomError) Error() string {
	return e.err
}

func (e *areaCustomError) lengthNegative() bool {
	return e.length < 0
}

func (e *areaCustomError) widthNegative() bool {
	return e.width < 0
}

func rectArea(length, width float64) (float64, error) {
	err := ""
	if length < 0 {
		err += "length is less than zero"
	}
	if width < 0 {
		if err == "" {
			err = "width is less than zero"
		} else {
			err += ", width is less than zero"
		}
	}

	if err != "" {
		return 0, &areaCustomError{err, length, width}
	}
	return length * width, nil
}

func TestRectArea(t *testing.T) {
	length, width := -5.0, -9.0
	area, err := rectArea(length, width)
	if err != nil {
		if err, ok := err.(*areaCustomError); ok {
			if err.lengthNegative() {
				t.Logf("error: length %0.2f is less than zero\n", err.length)
			}

			if err.widthNegative() {
				t.Logf("error: width %0.2f is less than zero\n", err.width)
			}
			return
		}
		t.Log(err)
		return
	}

	t.Log("area of rect", area)
}
