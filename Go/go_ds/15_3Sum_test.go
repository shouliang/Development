package ds

import (
	"sort"
	"testing"
)

func TestThreeSum(t *testing.T) {
	nums := []int{-1, 0, 1, 2, -1, -4}
	res := threeSum(nums)
	t.Log(res)
}

func threeSum(nums []int) [][]int {
	var res [][]int
	sort.Ints(nums) // 对原数组进行排序

	target := 0                        // 本题3数之和为0，也可以是3个之和为任意一个数n
	for i := 0; i < len(nums)-2; i++ { // 因为是3个数之和，i只需要从0循环到倒数第3个，即：len - 2
		if i > 0 && nums[i] == nums[i-1] { // 相邻的两个元素相等则跳过当前元素
			continue
		}
		left, right := i+1, len(nums)-1 // 注意 left 从 i+1 开始
		for left < right {
			diff := nums[i] + nums[left] + nums[right] - target
			if diff < 0 {
				left++
			} else if diff > 0 {
				right--
			} else {
				res = append(res, []int{nums[i], nums[left], nums[right]})
				left++
				right--
			}
		}
	}

	return res
}
