package main // 改变切片
import "fmt"

// 可变参数
func change(s ...string) {
	s[0] = "Go"
}

func main() {
	welcome := []string{"hello", "world"}

	// welcome...传入切片但不会创建新的切片
	change(welcome...)
	fmt.Println(welcome)
}
