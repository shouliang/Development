// 展示来自不同标准库的不同函数是如何使用io.Writer接口的
package main

import (
	"bytes"
	"fmt"
	"os"
)

func main() {
	var b bytes.Buffer
	b.Write([]byte("Hello "))

	fmt.Fprintf(&b, "World")
	b.WriteTo(os.Stdout)
}
