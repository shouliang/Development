package writefile01

import (
	"fmt"
	"os"
	"testing"
)

/*将字符串写入文件
最常见的写文件就是将字符串写入文件。这个写起来非常的简单。这个包含以下几个阶段。

1.创建文件
2.将字符串写入文件
*/
func TestWriteStringToFile(t *testing.T) {
	f, err := os.Create("test.txt")
	if err != nil {
		t.Log(err)
		return
	}

	l, err := f.WriteString("Hello World")
	if err != nil {
		t.Log(err)
		f.Close()
		return
	}

	t.Log(l, "bytes written successfully")
	err = f.Close()
	if err != nil {
		t.Log(err)
		return
	}
}

/*将字节写入文件
将字节写入文件和写入字符串非常的类似。我们将使用 Write 方法将字节写入到文件
*/
func TestWriteBytesToFile(t *testing.T) {
	f, err := os.Create("bytes")
	if err != nil {
		t.Log(err)
		return
	}
	d := []byte{104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100}
	n, err := f.Write(d)
	if err != nil {
		t.Log(err)
		f.Close()
		return
	}

	t.Log(n, "bytes written successfully")
	err = f.Close()
	if err != nil {
		t.Log(err)
		return
	}
}

/*将字符串一行一行的写入文件
另外一个常用的操作就是将字符串一行一行的写入到文件。
*/
func TestWriteFileByLineToLine(t *testing.T) {
	f, err := os.Create("lines")
	if err != nil {
		t.Log(err)
		f.Close()
		return
	}
	d := []string{"Welcome to the world of GO", "Go is a complied language", "It is easy to learn Go."}
	for _, v := range d {
		fmt.Fprintln(f, v) // 使用 Fprintln Fprintln 函数 将 io.writer 做为参数，并且添加一个新的行
		if err != nil {
			t.Log(err)
			return
		}
	}

	err = f.Close()
	if err != nil {
		t.Log(err)
		return
	}
	t.Log("file written successfully")
}

/*追加到文件
这一部分我们将追加一行到上节创建的 lines 文件中。
我们将追加 File handling is easy 到 lines 这个文件。

这个文件将以追加和写的方式打开。这些标志将通过 Open 方法实现。
当文件以追加的方式打开，我们添加新的行到文件里。
*/
func TestAppenToFile(t *testing.T) {
	f, err := os.OpenFile("lines", os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		t.Log(err)
		return
	}

	newline := "File handling is easy."
	_, err = fmt.Fprintln(f, newline)
	if err != nil {
		t.Log(err)
		f.Close()
		return
	}

	err = f.Close()
	if err != nil {
		t.Log(err)
		f.Close()
	}
	t.Log("file appended succesfully")
}
