package entities

// User首字母是大写，所以是公开的
type User struct {
	Name  string
	email string // email首字母非大写，所以不是公开的
}
