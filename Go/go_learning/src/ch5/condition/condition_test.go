package condition_test

import "testing"

func TestSwitchMultiCase(t *testing.T) {
	for i := 0; i < 5; i++ {
		switch i {
		case 0, 2: // 只要匹配其中一种即可，无break语句，但效果等同于其他语言中加了break语句
			t.Log("Even")
		case 1, 3:
			t.Log("Odd")
		default:
			t.Log("it is not 0-3")
		}
	}
}
func TestSwitchCaseCondition(t *testing.T) {
	for i := 0; i < 5; i++ {
		switch { // 类似于if else 语句
		case i%2 == 0:
			t.Log("Even")
		case i%2 == 1:
			t.Log("Odd")
		default:
			t.Log("unknow")
		}
	}
}
