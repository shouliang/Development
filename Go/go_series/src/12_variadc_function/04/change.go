package main // 改变切片
import "fmt"

// 可变参数
func change(s ...string) {
	s[0] = "Go"

	// 当新的元素被append到切片时，会创建一个新的数组。
	// 现有数组的元素被复制到这个新数组中，并返回这个新数组的新切片引用。
	s = append(s, "playground")
	fmt.Println(s) // Go world playground
}

func main() {
	welcome := []string{"hello", "world"}

	change(welcome...)
	fmt.Println(welcome) // Go world
}
