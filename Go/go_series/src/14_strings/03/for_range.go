// 字符串的for range 循环
// for range: 使用for range循环遍历了字符串,循环返回的是是当前 rune 的字节位置
// 所以打印汉字也不会出现乱码
package main

import "fmt"

func printCharsAndBytes(s string) {
	for index, r := range s {
		fmt.Printf("%c starts at byte %d\n", r, index)
	}
}

func main() {
	// 1个汉字占用3个字节
	china := "china中华人民共和国"
	printCharsAndBytes(china)
}
