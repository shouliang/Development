package mapstest

import "testing"

// map 是在 Go 中将值（value）与键（key）关联的内置类型。通过相应的键可以获取到值。
// make(map[type] value) 是创建 map 的语法。
func TestMakeMaps(t *testing.T) {
	// 声明一个map[string]int类型的变量personSalary
	var personSalary map[string]int

	// map的零值是nil
	if personSalary == nil {
		t.Log("map is nil. Going to make one.")

		// 如果你想添加元素到 nil map 中，会触发运行时 panic
		// personSalary["steve"] = 5000 // assignment to entry in nil map [recovered]

		// 使用make语法创建map
		personSalary = make(map[string]int)
		personSalary["steve"] = 5000
	}
}

// 给 map 添加元素
func TestMapsAdd(t *testing.T) {
	personSalary := make(map[string]int)

	// 向map中添加新元素
	personSalary["steve"] = 12000
	personSalary["jamie"] = 15000
	personSalary["mike"] = 9000
	t.Log("personSalary map contents:", personSalary)

	// 声明并初始化，而后添加
	personSalary2 := map[string]int{
		"zhangsan": 6666,
		"lisi":     7777,
	}
	personSalary2["wangwu"] = 8888
	t.Log("personSalar2 map contents:", personSalary2)
}

// 获取 map 中的元素
// 获取 map 元素的语法是 map[key]
func TestMapsGet(t *testing.T) {
	personSalary := map[string]int{
		"steve": 12000,
		"jamie": 15000,
	}
	personSalary["mike"] = 9000

	employee := "jamie"
	t.Log("Salary of", employee, "is", personSalary[employee])

	// 如果获取一个不存在的元素，map 会返回该元素类型的零值
	t.Log("Salary of joe is", personSalary["joe"])

	// value, ok := map[key]
	// 如果 ok 是 true，表示 key 存在，key 对应的值就是 value ，反之表示 key 不存在。
	newEmpee := "rose"
	value, ok := personSalary[newEmpee]
	if ok == true {
		t.Log("Salary of", newEmpee, "is", value)
	} else {
		t.Log(newEmpee, "is not found")
	}
}

// 遍历 map 使用for range 不保证每次执行程序获取的元素顺序相同。
func TestMapForRange(t *testing.T) {
	personSalary := map[string]int{
		"steve": 12000,
		"jamie": 15000,
		"mike":  9000,
	}
	for key, value := range personSalary {
		t.Logf("personSalary[%s] = %d\n", key, value)
	}
}

// 删除 map 中的元素
// 删除 map 中 key 的语法是 delete(map, key)。这个函数没有返回值。
func TestMapsDelete(t *testing.T) {
	personSalary := map[string]int{
		"steve": 12000,
		"jamie": 15000,
		"mike":  9000,
	}
	t.Log("map before deletion", personSalary)
	delete(personSalary, "steve")
	t.Log("map after deletion", personSalary)
}

// 获取 map 的长度
// 取 map 的长度使用 len 函数。
func TestMapsLen(t *testing.T) {
	personSalary := map[string]int{
		"steve": 12000,
		"jamie": 15000,
		"mike":  9000,
	}
	t.Log("length is ", len(personSalary))
}

// Map 是引用类型
/*
和 slices 类似，map 也是引用类型。
当 map 被赋值为一个新变量的时候，它们指向同一个内部数据结构。
因此，改变其中一个变量，就会影响到另一变量。
*/
func TestMapsAreReferenceTypes(t *testing.T) {
	personSalary := map[string]int{
		"steve": 12000,
		"jamie": 15000,
		"mike":  9000,
	}
	t.Log("Original person salary", personSalary)

	newPersonSalary := personSalary
	newPersonSalary["mike"] = 8888
	t.Log("personSalary changed", personSalary)
}

// 当 map 作为函数参数传递时也会发生同样的情况。
//函数中对 map 的任何修改，对于外部的调用都是可见的
func TestMapsPassToFunction(t *testing.T) {
	personSalary := map[string]int{
		"steve": 12000,
		"jamie": 15000,
		"mike":  9000,
	}
	t.Log("before function call personSalary is", personSalary)

	changed(personSalary)
	t.Log("after function call personSalary is ", personSalary)
}

func changed(m map[string]int) {
	m["jamie"] = 6666
}

// Map 的相等性
// map 之间不能使用 == 操作符判断，== 只能用来检查 map 是否为 nil。
// 判断两个 map 是否相等的方法是遍历比较两个 map 中的每个元素。我建议你写一段这样的程序实现这个功能
func TestMapsNotEqual(t *testing.T) {
	map1 := map[string]int{
		"one": 1,
		"two": 2,
	}

	map2 := map1
	t.Log("map2 is", map2)

	// invalid operation: map1 == map2 (map can only be compared to nil)
	// if map1 == map2 {
	//
	// }
	// == 只能用来检查 map 是否为 nil。
	if map1 == nil {
		t.Log("map1 is nil")
	} else {
		t.Log("map1 is not nil")
	}
}
