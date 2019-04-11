package loops

import (
	"testing"
)

// for 是 Go 语言唯一的循环语句。Go 语言中并没有其他语言比如 C 语言中的 while 和 do while 循环。
// for 循环语法
// for initialisation; condition; post {
// }
// initialisation 初始化语句只执行一次,post是可选的

func TestLoops(t *testing.T) {
	for i := 0; i <= 10; i++ {
		t.Logf(" %d", i)
	}
}

// break
// break 语句用于在完成正常执行之前突然终止 for 循环
func TestLoopsWithBreak(t *testing.T) {
	for i := 1; i <= 10; i++ {
		if i > 5 {
			break
		}
		t.Logf("%d", i)
	}
	t.Log("\n line after loop")
}

// continue
// continue 语句用来跳出 for 循环中当前循环。
func TestLoopsWithContinue(t *testing.T) {
	for i := 1; i <= 10; i++ {
		// 如果是偶然就跳出当前循环，进入下一次循环
		if i%2 == 0 {
			continue
		}
		t.Logf("%d", i)
	}
}

// 更多 关于循环
func TestLoopsWithMore(t *testing.T) {
	// 可以省略初始化 和 循环增加语句
	// i := 0
	// for ;i <= 10; {
	// 	t.Logf("%d ", i)
	// 	i += 2
	// }

	// 还可以省略分号; 此时 for 相当于 while
	i := 0
	for i <= 10 {
		t.Logf("%d ", i)
		i += 2
	}

	// 在 for 循环中可以声明和操作多个变量
	for no, i := 10, 1; i <= 10 && no <= 19; i, no = i+1, no+1 { //multiple initialisation and increment
		t.Logf("%d * %d = %d\n", no, i, no*i)
	}

	// 无限循环
	// for {
	//
	// }

}
