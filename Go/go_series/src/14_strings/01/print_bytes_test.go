// 单独获取字符串的每一个字节
// 由于字符串是一个字节切片，所以我们可以获取字符串的每一个字节。
package main

import (
	"fmt"
	"testing"
)

// %x 以十六进制打印每个字节
func printBytes(s string) {
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
}

// %c 以字符形式打印字符串中的每一个字符
// 但是1个汉字会占用3个字节，逐个打印汉字会出现乱码
func printChars(s string) {
	for i := 0; i < len(s); i++ {
		fmt.Printf("%c ", s[i])
	}
}

func TestBytes(t *testing.T) {
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
