// 用 rune 切片构造字符串
package main

import (
	"fmt"
	"testing"
)

func TestConstructFromRune(t *testing.T) {
	runeSlice := []rune{0x0053, 0x0065, 0x00f1, 0x006f, 0x0072}
	str := string(runeSlice)
	fmt.Println(str)
}
