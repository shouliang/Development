package entities

type user struct {
	Name  string // 首字母大写
	Email string // 首字母大写
}

// Admin首字母大写，可访问
type Admin struct {
	user   // 嵌入的类型是未公开的
	Rights int
}
