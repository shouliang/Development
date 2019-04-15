package reflection02

import (
	"fmt"
	"reflect"
	"testing"
)

type order struct {
	ordId      int
	customerId int
}

/*reflect 包
在 Go 语言中，reflect 实现了运行时反射。reflect 包会帮助识别 interface{} 变量的底层具体类型和具体值。

reflect.Type 和 reflect.Value
reflect.Type 表示 interface{} 的具体类型，而 reflect.Value 表示它的具体值。
*/

func createQuery(q interface{}) {
	t := reflect.TypeOf(q)
	v := reflect.ValueOf(q)
	fmt.Println("Type ", t)
	fmt.Println("Value ", v)
}

func TestQueryReflectTypeAndReflectValue(t *testing.T) {
	o := order{
		ordId:      1234,
		customerId: 567,
	}
	createQuery(o)
}
