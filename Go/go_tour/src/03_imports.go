// 导入
package main

// 用圆括号组合导入，这是“打包”导入语句
import (
	"fmt"
	"math"
)

// 也可以编写多个导入语句，不过使用"打包"导入语句是更好的形式
// import "fmt"
// import "math"

func main() {
	fmt.Printf("Now you have %g problems.", math.Nextafter(2, 3))
}
