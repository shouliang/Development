// basename 移除路径部分和 .后缀: 利用库函数 string.LastIndex
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	input := bufio.NewScanner(os.Stdin)
	for input.Scan() {
		fmt.Println(basename(input.Text()))
	}
}

// basename 移除路径部分和 .后缀: 利用库函数 string.LastIndex
func basename(s string) string {
	slash := strings.LastIndex(s, "/") // 如果没有找到"/",则slash取值-1
	s = s[slash+1:]
	if dot := strings.LastIndex(s, "."); dot >= 0 {
		s = s[:dot]
	}
	return s
}
