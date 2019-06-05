// echo2 输出其命令行参数
package main

import (
	"fmt"
	"os"
)

func main() {
	var s, sep string
	for _, arg := range os.Args[1:] {
		s += sep + arg
		sep = " "
	}
	fmt.Println(s)
}
