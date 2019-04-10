package main // 改变切片
import "fmt"

// 可变参数
func change(s ...string) {
	s[0] = "Go"
}

func main() {
	welcome := []string{"hello", "world"}

	// welcome...三个点的形式传入切片类型，不会创建新的切片
	change(welcome...)
	fmt.Println(welcome)
}
