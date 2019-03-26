// 如何使用io.Reader和io.Writer接口
// 写一个简单版本的curl程序
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func init() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: ./example <url>")
		os.Exit(-1)
	}
	// fmt.Println(os.Args[0])
	// fmt.Println(os.Args[1])
}

// go run listing34.go https://www.baidu.com
func main() {
	// 从web服务器得到响应
	r, err := http.Get(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}

	// 从Body复制到Stdout
	io.Copy(os.Stdout, r.Body)
	if err := r.Body.Close(); err != nil {
		fmt.Println(err)
	}
}
