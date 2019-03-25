// 修改 map
package main

import "fmt"

func main() {
	m := make(map[string]int)

	// 插入或者修改一个元素   m[key] = value
	m["Answer"] = 42
	fmt.Println("The value:", m["Answer"])

	// 获取元素 elem = m[key]
	m["Answer"] = 48
	fmt.Println("The value:", m["Answer"])

	// 删除元素
	delete(m, "Answer")
	fmt.Println("The value:", m["Answer"])

	// 通过双赋值检测某个键是否存在，ok为false时，value为其对应的零值
	v, ok := m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)
}
