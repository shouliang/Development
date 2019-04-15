package reflection03

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

relfect.Kind
reflect 包中还有一个重要的类型：Kind。
*/

// Type 表示 interface{} 的实际类型（在这里是 reflection03.order)，
// 而 Kind 表示该类型的特定类别（在这里是 struct）
func createQuery(q interface{}) {
	t := reflect.TypeOf(q)
	k := t.Kind()
	fmt.Println("Type ", t)
	fmt.Println("Kind ", k)
}

func TestQueryReflectKind(t *testing.T) {
	o := order{
		ordId:      1234,
		customerId: 567,
	}
	createQuery(o)
}

/*NumField() 和 Field() 方法
NumField() 方法返回结构体中字段的数量，而 Field(i int) 方法返回字段 i 的 reflect.Value。
*/
func createQueryField(q interface{}) {
	if reflect.ValueOf(q).Kind() == reflect.Struct {
		v := reflect.ValueOf(q)
		for i := 0; i < v.NumField(); i++ {
			fmt.Printf("Field:%d type:%T value:%v\n", i, v.Field(i), v.Field(i))
		}
	}
}

func TestReflectNumField(t *testing.T) {
	o := order{
		ordId:      1234,
		customerId: 567,
	}
	createQueryField(o)
}

// Int() 和 String() 方法
// Int 和 String 可以帮助我们分别取出 reflect.Value 作为 int64 和 string。
func TestReflectIntAndString(t *testing.T) {
	a := 56
	x := reflect.ValueOf(a).Int()
	t.Logf("type:%T value:%v\n", x, x)

	b := "zhangsan"
	y := reflect.ValueOf(b).String()
	t.Logf("type:%T value:%v\n", y, y)
}
