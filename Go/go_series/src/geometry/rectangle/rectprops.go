// 属于某一个包的源文件都应该放置于一个单独命名的文件夹里。
// 按照 Go 的惯例，应该用包名命名该文件夹。
// 在 Go 中，任何以大写字母开头的变量或者函数都是被导出的名字
package rectangle

import "math"

// 计算矩形面积
func Area(len, wid float64) float64 {
	area := len * wid
	return area
}

// 计算矩形对角线长度
func Diagonal(len, wid float64) float64 {
	diagonal := math.Sqrt((len * len) + (wid * wid))
	return diagonal
}
