// 排序
// Go 的 sort 包实现了内置和用户自定义数据类型的排序功能。
package main

import (
	"fmt"
	"sort"
)

func main() {
	// 排序是原地更新的，所以他会改变给定的序列并且不返回一个新值。
	strs := []string{"c", "a", "b"}
	sort.Strings(strs)
	fmt.Println("Strings:", strs)

	ints := []int{7, 2, 4}
	sort.Ints(ints)
	fmt.Println("Ints:", ints)

	// 判断是否已经排好序
	sorted := sort.IntsAreSorted(ints)
	fmt.Println("Sorted:", sorted)

	sorted = sort.IntsAreSorted([]int{1, 5, 3})
	fmt.Println("Sorted:", sorted)
}
