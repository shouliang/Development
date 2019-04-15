// 什么是反射？ 反射就是程序能够在运行时检查变量和值，求出它们的类型
package reflection01

import (
	"fmt"
	"testing"
)

type order struct {
	ordId      int
	customerId int
}

func createQuery(o order) string {
	sql := fmt.Sprintf("insert into order values(%d,%d)", o.ordId, o.customerId)
	return sql
}

func TestQuery(t *testing.T) {
	o := order{
		ordId:      1234,
		customerId: 567,
	}
	t.Log(createQuery(o))
}
