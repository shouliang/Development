/*使用命令行标记来传递文件路径
另一种解决方案是使用命令行标记来传递文件路径。使用 flag 包，我们可以从输入的命令行获取到文件路径，接着读取文件内容。

首先我们来看看 flag 包是如何工作的。flag 包有一个名为 String 的函数。
该函数接收三个参数。第一个参数是标记名，第二个是默认值，第三个是标记的简短描述。
*/
package main

import (
	"flag"
	"fmt"
	"io/ioutil"
)

func main() {
	fptr := flag.String("fpath", "test.txt", "file path to read from")
	flag.Parse()

	data, err := ioutil.ReadFile(*fptr)
	if err != nil {
		fmt.Println("File reading error", err)
		return
	}
	fmt.Println("Contents of file:", string(data))
}
