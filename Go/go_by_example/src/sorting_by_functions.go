// 自定义函数排序
package main

import (
	"fmt"
	"sort"
)

// 自定义类型ByLength
type ByLength []string

// 自定义类型ByLength实现了 sort.Interface 的 Len，Less和 Swap 方法，
// 这样我们就可以使用 sort 包的通用Sort 方法
func (s ByLength) Len() int {
	return len(s)
}

func (s ByLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

// 自定义按字符串长度来排序
func (s ByLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

func main() {
	fruits := []string{"peach", "banana", "kiwi"}
	sort.Sort(ByLength(fruits))
	fmt.Println(fruits)
}
