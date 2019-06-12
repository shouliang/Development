// echo4 输出其命令行参数
package main

import (
	"flag"
	"fmt"
	"strings"
)

// n 标识换行： 设置false,则其不换行
var n = flag.Bool("n", false, "omit trailing newline")
var sep = flag.String("s", " ", "separator")

func main() {
	// 更新标识变量的默认值
	flag.Parse()
	fmt.Print(strings.Join(flag.Args(), *sep))
	if !*n {
		fmt.Println()
	}
}
