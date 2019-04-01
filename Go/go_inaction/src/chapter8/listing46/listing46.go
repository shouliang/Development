// 展示如何使用io.Reader和io.Writer接口写一个简单版本的curl
package main

import (
	"io"
	"log"
	"net/http"
	"os"
)

// go run listing46.go https:www.baidu.com httpget.txt
func main() {
	r, err := http.Get(os.Args[1])
	if err != nil {
		log.Fatalln(err)
	}

	file, err := os.Create(os.Args[2])
	if err != nil {
		log.Fatalln(err)
	}

	defer file.Close()

	dest := io.MultiWriter(os.Stdout, file)
	io.Copy(dest, r.Body)

	if err := r.Body.Close(); err != nil {
		log.Println(err)
	}
}
