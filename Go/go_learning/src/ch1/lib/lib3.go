package lib

// 首字母大写程序实体才可以被外部调用，即是公开的
func HelloFromLib3() string {
	return "hello from lib3"
}

// 首字母小写，私有
func helloFromLib3() string {
	return "hello from lib3 with lowercase"
}
