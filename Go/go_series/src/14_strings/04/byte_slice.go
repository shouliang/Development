// 用字节切片构造字符串
package main

import "fmt"

func main() {
	// byteSlice := []byte{0x43, 0x61, 0x66, 0xC3, 0xA9} // 十六进制
	byteSlice := []byte{67, 97, 102, 195, 169} // 十进制
	str := string(byteSlice)
	fmt.Println(str)
}
