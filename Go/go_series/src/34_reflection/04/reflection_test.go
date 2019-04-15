package reflection04

import (
	"fmt"
	"reflect"
	"testing"
)

// 完整的程序

type order struct {
	ordId      int
	customerId int
}

type employee struct {
	name    string
	id      int
	address string
	salary  int
	country string
}

func createQuery(q interface{}) {
	if reflect.ValueOf(q).Kind() == reflect.Struct {
		t := reflect.TypeOf(q).Name()
		query := fmt.Sprintf("insert into %s values(", t)

		v := reflect.ValueOf(q)
		for i := 0; i < v.NumField(); i++ {
			switch v.Field(i).Kind() {
			case reflect.Int:
				if i == 0 {
					query = fmt.Sprintf("%s%d", query, v.Field(i).Int())
				} else {
					query = fmt.Sprintf("%s, %d", query, v.Field(i).Int())
				}
			case reflect.String:
				if i == 0 {
					query = fmt.Sprintf("%s\"%s\"", query, v.Field(i).String())
				} else {
					query = fmt.Sprintf("%s, \"%s\"", query, v.Field(i).String())
				}
			default:
				fmt.Println("Unsupported type")
				return
			}
		}

		query = fmt.Sprintf("%s)", query)
		fmt.Println(query)
		return
	}

	// 作了额外的检查，以防止 createQuery 函数传入不支持的类型时，程序发生崩溃
	fmt.Println("unsupported type")
}

func TestReflection(t *testing.T) {
	o := order{
		ordId:      456,
		customerId: 789,
	}
	createQuery(o)

	e := employee{
		name:    "zhangsan",
		id:      111,
		address: "guoding Road",
		salary:  10000,
		country: "China",
	}
	createQuery(e)

	i := 99
	createQuery(i)

}

/*
我们应该使用反射吗？
我们已经展示了反射的实际应用，现在考虑一个很现实的问题。我们应该使用反射吗？
我想引用 Rob Pike 关于使用反射的格言，来回答这个问题。

清晰优于聪明。而反射并不是一目了然的。

反射是 Go 语言中非常强大和高级的概念，我们应该小心谨慎地使用它。
使用反射编写清晰和可维护的代码是十分困难的。你应该尽可能避免使用它，只在必须用到它时，才使用反射。
*/
