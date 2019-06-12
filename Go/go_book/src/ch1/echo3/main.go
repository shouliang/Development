// echo3 输出其命令行参数: 使用strings包中的Join函数
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println(strings.Join(os.Args[1:], " "))

	// 不关心格式可以直接输出  os.Args []string
	fmt.Println(os.Args[1:])
}
