package computer

// 结构体首字母大写，为导出类型
type Spec struct {
	Maker string // 字段首字母大写，为导出类型
	model string // 字段首字母小写，为非导出类型
	Price int    // 字段首字母大写，为导出类型
}
