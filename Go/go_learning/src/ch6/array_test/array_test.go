// 数组初始化和遍历，数组容量不可收缩
package array_test

import "testing"

func TestArrayInit(t *testing.T) {
	// 数组初始化，全部为0
	var arr [3]int

	// 初始化并赋值
	arr1 := [4]int{1, 2, 3, 5}

	// [...] 可以不指定数组的长度
	arr2 := [...]int{5, 8, 9, 4}

	arr1[1] = 4
	t.Log(arr1[1], arr2[1])
	t.Log(arr)
}

func TestArrayTravel(t *testing.T) {
	arr3 := [...]int{1, 3, 4, 5}

	// 第一种遍历的做法
	// for i := 0; i < len(arr3); i++ {
	// 	t.Log(arr3[i])
	// }

	// 推荐第二种遍历的做法：使用for rang,不需要索引可以通过下划线_舍弃
	for index, e := range arr3 {
		t.Log(index, e)
	}

	for _, e := range arr3 {
		t.Log(e)
	}
}

func TestArraySection(t *testing.T) {
	arr := [...]int{5, 8, 4, 7, 6, 3}
	arr_section := arr[0:3]
	t.Log(arr_section)
	arr_section = arr[:3]
	t.Log(arr_section)
	arr_section = arr[3:]
	t.Log(arr_section)
	arr_section = arr[:]
	t.Log(arr_section)
}
