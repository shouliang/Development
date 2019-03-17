package service

import "fmt"

// 同一个源文件可以多次定义init方法
func init(){
	fmt.Println("init 1 from service")
}

func init(){
	fmt.Println("init 2 from service")
}

// func square(n int) int{
// 	return n * n
// }

// 公用的函数名首字母必须是大写
func Square(n int) int{
	return n * n
}

func GetFibnacciService(n int) []int {
	ret := []int{1, 1}
	for i := 2; i < n; i++ {
		ret = append(ret, ret[i-2]+ret[i-1])
	}
	return ret
}
