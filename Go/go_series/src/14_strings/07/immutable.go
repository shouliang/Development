// 为了修改字符串，可以把字符串转化为一个 rune 切片。
// 然后这个切片可以进行任何想要的改变，然后再转化为一个字符串
package main

import "fmt"

func mutate(s []rune) string {
	s[0] = 'a'
	return string(s)
}

func main() {
	h := "hello"
	fmt.Println(mutate([]rune(h)))
}
