package pool

import (
	"fmt"
	"testing"
	"time"
)

func TestObjPool(t *testing.T) {
	pool := NewObjPool(10)

	// 还未使用，就尝试放置超过池大小的对象，会出现overflow错误
	// if err := pool.ReleaseObj(&ReusableObj{}); err != nil {
	// 	t.Error(err)
	// }

	// 获取超过池大小的对象，也会出现错误
	for i := 0; i < 11; i++ {
		if v, err := pool.GetObj(time.Second * 1); err != nil {
			t.Error(err)
		} else {
			fmt.Printf("%T\n", v)

			// if err := pool.ReleaseObj(v); err != nil {
			// 	t.Error(err)
			// }

		}
	}
}
