// 切片：共享的存储结构,自增长
package slice_test

import "testing"

func TestSliceInit(t *testing.T) {
	// 切片和数组的声明很类似，但是没有指明长度
	var s0 []int
	t.Log(len(s0), cap(s0))

	s0 = append(s0, 2)
	t.Log(len(s0), cap(s0))

	s1 := []int{1, 2, 3, 4}
	t.Log(len(s1), cap(s1))

	// make创建切片，初始化 len=3, cap=5
	s2 := make([]int, 3, 5)
	t.Log(len(s2), cap(s2))
	// 只可以访问len索引内的
	t.Log(s2[0], s2[1], s2[2])
	// t.Log(s2[0], s2[1], s2[2], s2[3])

	// append一个元素后，len也相应的增长，故可以访问s2[3]了
	s2 = append(s2, 9)
	t.Log(len(s2), cap(s2))
	t.Log(s2[0], s2[1], s2[2], s2[3])
}

func TestSliceGrowing(t *testing.T) {
	s := []int{}
	for i := 0; i < 10; i++ {
		// 在cap<1024,cap空间不够时，会增长2倍,而后增长1.25倍
		s = append(s, i)
		t.Log(len(s), cap(s))
	}
}

func TestSliceShareMemory(t *testing.T) {
	year := []string{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
	Q2 := year[3:6]
	t.Log(Q2, len(Q2), cap(Q2))

	summer := year[5:8]
	t.Log(summer, len(summer), cap(summer))

	// 修改后会影响到其他的共享的切片
	summer[0] = "Unknow"
	t.Log(Q2)
}

func TestSliceComparing(t *testing.T) {
	// a := []int{1, 3, 2, 4}
	// b := []int{1, 3, 2, 4}

	// 以下语句的报错信息：slice can only be compared to nil 切片只能和nil进行比较
	// if a == b {
	//
	// }

}
