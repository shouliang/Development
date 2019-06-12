// nonempty 演示了slice的就地修改算法
package main

import "fmt"

func main() {
	data := []string{"one", "", "three"}
	fmt.Printf("%q\n", nonempty(data))
	fmt.Printf("%q\n", data)

	s := []int{5, 6, 7, 8, 9}
	fmt.Println(remove(s, 2))
}

// nonempty返回一个新的slice,slice中的元素都是非空字符串
func nonempty(strings []string) []string {
	i := 0
	for _, s := range strings {
		if s != "" {
			strings[i] = s
			i++
		}
	}
	return strings[:i]
}

func remove(slice []int, i int) []int {
	copy(slice[i:], slice[i+1:])
	return slice[:len(slice)-1]
}
