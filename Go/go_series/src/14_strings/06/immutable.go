// 字符串是不可变的
package main

import "fmt"

func mutate(s string) string {
	s[0] = 'a' // cannot assign to s[0]
	return string(s)
}

func main() {
	h := "hello"
	fmt.Println(mutate(h))
}
