/* 将文件绑定在二进制文件中
虽然从命令行获取文件路径的方法很好，但还有一种更好的解决方法。如果我们能够将文本文件捆绑在二进制文件，
岂不是很棒？这就是我们下面要做的事情。

有很多包可以帮助我们实现。我们会使用 packr，因为它很简单
*/
package main

import (
	"fmt"

	"github.com/gobuffalo/packr"
)

func main() {
	box := packr.NewBox("../filehandling03")
	data := box.String("test.txt")
	fmt.Println("Contents of file:", string(data))
}
