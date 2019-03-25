package main

import (
	"chapter3/words"
	"fmt"
	"io/ioutil"
	"os"
)

// go run wordcount.go  gowords.txt
func main() {
	// 获取命令行文件名
	filename := os.Args[1]

	contents, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("打开文件出错", err)
	}

	text := string(contents)
	fmt.Println(text)
	fmt.Println(words.CountWords(text))
}
