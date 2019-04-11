package switchtest

import "testing"

// switch 是一个条件语句，用于将表达式的值与可能匹配的选项列表进行比较，
// 并根据匹配情况执行相应的代码块。它可以被认为是替代多个 if else 子句的常用方式。
func TestSwitch(t *testing.T) {
	finger := 4
	switch finger {
	case 1:
		t.Log("Thumb")
	case 2:
		t.Log("Index")
	case 3:
		t.Log("Middle")
	case 4:
		t.Log("Ring")
	// 	// 在选项列表中，case 不允许出现重复项
	// case 4:
	// 	t.Log("Another Ring")
	case 5:
		t.Log("Pinky")
	default:
		t.Log("incorrect finger number")
	}
}

// 默认情况（Default Case）
func TestSwitchWithDefault(t *testing.T) {
	finger := 8
	switch finger {
	case 1:
		t.Log("Thumb")
	case 2:
		t.Log("Index")
	case 3:
		t.Log("Middle")
	case 4:
		t.Log("Ring")
	case 5:
		t.Log("Pinky")
	default:
		t.Log("incorrect finger number")
	}
}

// 多表达式判断
// 通过用逗号分隔，可以在一个 case 中包含多个表达式。
// 只有匹配其中任意一项即可命中
func TestSwitchWithMultipleExpressions(t *testing.T) {
	letter := "i"
	switch letter {
	case "a", "e", "i", "o", "u":
		t.Log("vowel")
	default:
		t.Log("not a vowel")
	}
}

// 无表达式的 switch
// 在 switch 语句中，表达式是可选的，可以被省略。
// 如果省略表达式，则表示这个 switch 语句等同于 switch true，并且每个 case 表达式都被认定为有效，相应的代码块也会被执行。
// 这种类型的 switch 语句可以替代多个 if else 子句。
func TestExpressionlessSwitch(t *testing.T) {
	num := 75
	switch {
	case num >= 0 && num <= 50:
		t.Log("num is greater than 0 and less than 50")
	case num >= 51 && num <= 100:
		t.Log("num is greater than 51 and less than 100")
	case num >= 100:
		t.Log("num is greater than 101")
	}
}

// 在 Go 中，每执行完一个 case 后，会从 switch 语句中跳出来，不再做后续 case 的判断和执行。
// 使用 fallthrough 语句可以在已经执行完成的 case 之后，把控制权转移到下一个 case 的执行代码中。
func TestFallThrough(t *testing.T) {
	switch num := number(); {
	case num < 50:
		t.Logf("%d is lesser than 50\n", num)
		fallthrough
	case num < 100:
		t.Logf("%d is lesser than 100\n", num)
		fallthrough
	case num < 200:
		t.Logf("%d is lesser than 200\n", num)
	}
}

func number() int {
	num := 15 * 5
	return num
}
