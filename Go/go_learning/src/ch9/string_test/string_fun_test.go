package string_test

import (
	"strconv"
	"strings"
	"testing"
)

func TestStringFn(t *testing.T) {
	s := "A,B,C"
	// 字符串切割
	parts := strings.Split(s, ",")
	t.Log("parts is", parts)
	for _, part := range parts {
		t.Log(part)
	}

	// 字符串连接
	t.Log(strings.Join(parts, "-"))
}

// 字符串与整数相互转换
func TestConv(t *testing.T) {
	s := strconv.Itoa(10)
	t.Log("str " + s)

	if i, err := strconv.Atoi("10"); err == nil {
		t.Log(i)
	}
}

func TestStringToRune(t *testing.T) {
	s := "中华人共和国"
	// for range 自动将字符串转换成rune
	// 2个都是1表示都是使用第1个参数输出，只是输出的格式不一样
	for _, c := range s {
		t.Logf("%[1]c %[1]d", c)
	}
}
