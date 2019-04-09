// rune 是 Go 语言的内建类型，它也是 int32 的别称。
// 在 Go 语言中，rune 表示一个代码点。代码点无论占用多少个字节，都可以用一个 rune 来表示
package main

import "fmt"

// %x 以十六进制打印每个字节
func printBytes(s string) {
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
}

// 打印rune切片，汉字就不会出现乱码
func printChars(s string) {
	runes := []rune(s)
	for i := 0; i < len(runes); i++ {
		fmt.Printf("%c ", runes[i])
	}
}

func main() {
	name := "Hello World"
	printBytes(name)
	fmt.Printf("\n")
	printChars(name)
	fmt.Printf("\n")

	china := "I love china 中国"
	printBytes(china)
	fmt.Printf("\n")
	printChars(china)
	fmt.Printf("\n")

}
