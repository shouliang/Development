/* 分块读取文件
在前面的章节，我们学习了如何把整个文件读取到内存。
当文件非常大时，尤其在 RAM 存储量不足的情况下，把整个文件都读入内存是没有意义的。
更好的方法是分块读取文件。这可以使用 bufio 包来完成。
*/
package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
)

func main() {
	fptr := flag.String("fpath", "test.txt", "file path to read from")
	flag.Parse()

	f, err := os.Open(*fptr)
	if err != nil {
		log.Fatal(err)
	}

	defer func() {
		if err = f.Close(); err != nil {
			log.Fatal(err)
		}
	}()

	r := bufio.NewReader(f)
	b := make([]byte, 3)
	for {
		// 以 3 个字节的块为单位读取 test.txt 文件
		_, err := r.Read(b)
		if err != nil {
			fmt.Println("Error reading file:", err)
			break
		}
		fmt.Println(string(b))
	}

}
