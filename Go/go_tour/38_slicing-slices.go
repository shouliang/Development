// 对slice切片
/*
	slice可以重新切片，创建一个新的slice值指向相同的数组
	表达式 s[lo:hi] 表示的是从lo到hi-1的slice元素
*/
package main

import "fmt"

func main() {
	p := []int{2, 3, 5, 7, 11, 13}
	fmt.Println("p == ", p)

	p1 := p[1:4] // 新的slice p1指向的数组就是之前slice p指向的数组
	p1[2] = 555  // 所以改变p1的值，同样也会改变p的值
	fmt.Println("p == ", p)

	fmt.Println("p[1:4] == ", p[1:4])
	fmt.Println("p[:3] == ", p[:3]) // 省略下标，表示从0开始
	fmt.Println("p[4:] == ", p[4:]) // 省略上标，表示到len(p)结束
}
