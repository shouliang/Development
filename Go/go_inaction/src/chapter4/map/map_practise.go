package main

import "fmt"

func main() {
	// 创建map 1：make
	dict := make(map[string]int)
	// 使用map
	dict["zhangsan"] = 26
	dict["lisi"] = 31
	fmt.Println(dict)

	// 创建map 2:字面量
	dict1 := map[string]string{"Red": "#da1337", "Orange": "#e95a22"}
	fmt.Println(dict1)

	// 不能作为键：切片、函数以及包含切片的结构类型
	// 键的类型是字符串切片，不可以，会报错
	// dict2 := map[[]string]int{}  // invalid map key type []string

	// 值类型：只要值可以进行 == 运算符比较即可

	// 声明但是为初始化会创建一个值为nil的map
	// nil映射不能用于存储键值对，会产生一个运行时错误
	var colors map[string]string
	// colors["Red"] = "#da1337" // panic: assignment to entry in nil map
	fmt.Println(colors == nil)

	// map 中即使该键不存在，也不会报错，而是会返回相对于类型的零值
	value := dict1["Blue"]
	fmt.Println("value == \"\" is ", value == "")

	// 或者 返回两个值，第二个值表示该键是否存在
	value1, exisit := dict1["Blue"]
	if exisit {
		fmt.Println(value1)
	} else {
		fmt.Println("not exist Blue")
	}

	// 迭代 for range
	dict2 := map[string]string{
		"AliceBlue":   "#f0f8ff",
		"Coral":       "#ff7F50",
		"DarkGray":    "#a9a9a9",
		"ForestGreen": "#228b22", // map最后一个元素必须有一个包括一个貌似多余的逗号,
	}
	for key, value := range dict2 {
		fmt.Println(key, value)
	}

	removeColor(dict2, "Coral")
	delete(dict2, "Coral111") // 删除不存在的键也不会报错
	fmt.Println("----------------")
	for key, value := range dict2 {
		fmt.Println(key, value)
	}

}

// 在函数间传递map并不会制造出该映射的一个副本
// 修改了map，所有对这个map的引用都会觉察到这个修改
func removeColor(colors map[string]string, key string) {
	delete(colors, key)
}
