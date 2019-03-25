package string_test

import "testing"

func TestString(t *testing.T) {
	var s string
	// string是数据类型，初始化默认零值“”
	t.Log(s)

	s = "hello"
	t.Logf("len hello is %d", len(s))

	//cannot assign to s[1],因为 string是只读的byte slice(字节切片)
	// s[1] = 'a'

	// string的byte数组可以存储任何数据(包括二进制数据)
	s = "\xE4\xBA\xA5"
	// 虽然可能会出现乱码
	// s = "\xE4\xBA\xBB\xFF"
	t.Log(s)
	t.Logf("len of s is changed to %d", len(s))

	// len函数计算的是其包含的byte数，此处1个汉字为3个byte
	s = "中"
	t.Logf("汉字'中'的len是 %d", len(s))

	//字符串转换成 rune的切片, rune能够取出字符串中的unicode,此处汉字'中'的unicode编码长度为1
	c := []rune(s)
	t.Logf("汉字'中'rune后的len是 %d", len(c))

	// %x 表示十六进制
	t.Logf("汉字'中'的 unicode %x", c[0])
	t.Logf("汉字'中'的 UTF8 %x", s)

}
