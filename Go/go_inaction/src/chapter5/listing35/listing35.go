// 展示bytes.Buffer也可以用于io.Copy函数
package main

import (
	"bytes"
	"fmt"
	"io"
	"os"
)

func main() {
	var b bytes.Buffer

	// 将字符串写入Buffer
	b.Write([]byte("Hello"))

	// 使用Fprintf将字符串拼接到Buffer
	fmt.Fprint(&b, "World!")

	// 将Buffer的内容写到Stdout
	io.Copy(os.Stdout, &b)
}
