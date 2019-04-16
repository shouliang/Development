/*将整个文件读取到内存
将整个文件读取到内存是最基本的文件操作之一。
这需要使用 ioutil 包中的 ReadFile 函数。
*/
package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	// 如果不是在当前目录运行，则会报错：找不到该文件
	//data, err := ioutil.ReadFile("test.txt")

	// 1.使用绝对路径
	// 它的缺点是：文件必须放在程序指定的路径中，否则就会出错。
	data, err := ioutil.ReadFile("/Users/admin/Downloads/Development/Go/go_series/src/35_reading_files/filehandling/test.txt")

	if err != nil {
		fmt.Println("File reading error", err)
		return
	}
	fmt.Println("Contents of file:", string(data))
}
