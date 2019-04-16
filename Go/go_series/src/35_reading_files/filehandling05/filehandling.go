/*逐行读取文件
本节我们讨论如何使用 Go 逐行读取文件。这可以使用 bufio 来实现。

逐行读取文件涉及到以下步骤。
1.打开文件；
2.在文件上新建一个 scanner；
3.扫描文件并且逐行读取。
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

	s := bufio.NewScanner(f)

	for s.Scan() {
		fmt.Println(s.Text())
	}

	// 当 Scan 返回 false 时，除非已经到达文件末尾（此时 Err() 返回 nil），
	// 否则 Err() 就会返回扫描过程中出现的错误。
	err = s.Err()
	if err != nil {
		log.Fatal(err)
	}

}
