// 导出名
// 在导入一个包后，就可以用其导出的名称来调用它
// 在Go中，首字母大写的名称是被导出的
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.Pi)
}
