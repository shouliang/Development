package ifelse

import "testing"

//f 是条件语句。if 语句的语法是
// if condition {
// }
// Go 语言里的 { } 是必要的，即使在 { } 之间只有一条语句。
func TestIfElse(t *testing.T) {
	num := 10
	if num%2 == 0 {
		t.Log("the number is even")
	} else { //else 语句应该在 if 语句的大括号 } 之后的同一行中。如果不是，编译器会不通过。出错的原因是 Go 语言的分号是自动插入
		t.Log("the number is odd")
	}
}

// if 还有另外一种形式，它包含一个 statement 可选语句部分，该组件在条件判断之前运行。它的语法是
// if statement; condition {
// }

// num 在 if 语句中进行初始化，num 只能从 if 和 else 中访问。
// 也就是说 num 的范围仅限于 if else 代码块。如果我们试图从其他外部的 if 或者 else 访问 num,编译器会不通过。
func TestIfElseWithStatement(t *testing.T) {
	if num := 10; num%2 == 0 {
		t.Log("the number is even")
	} else {
		t.Log("the number is odd")
	}

	// t.Log("num is", num) //  undefined: num
}
