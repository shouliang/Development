// 基准测试：比较哪个函数可以更好地将数字转换成字符串
// 需要引入testing包，函数签名为 *testing.B类型
// 文件也是xxx_test.go
// 函数名以 Benchmark 开始
// go test -bench=. [-bench=3s] 通配符.表示运行所有的基准方法，默认1秒
package listing28

import (
	"fmt"
	"strconv"
	"testing"
)

func BenchmarkSprintf(b *testing.B) {
	number := 10
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		fmt.Sprintf("%d", number)
	}
}

func BenchmarkFormat(b *testing.B) {
	number := int64(10)
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		strconv.FormatInt(number, 10)
	}
}

func BenchmarkItoa(b *testing.B) {
	number := 10
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		strconv.Itoa(number)
	}
}
