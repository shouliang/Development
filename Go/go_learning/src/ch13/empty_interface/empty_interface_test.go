// 空接口
// 空接口可以表示任何类型
// 通过断言来将空接口转换为指定类型
package empty_interface

import (
	"fmt"
	"testing"
)

func DoSomething(p interface{}) {
	// if i, ok := p.(int); ok { // 断言
	// 	fmt.Println("Integer", i)
	// 	return
	// }
	// if s, ok := p.(string); ok {
	// 	fmt.Println("string", s)
	// 	return
	// }
	//
	// fmt.Println("Unknow Type")

	// 可以将if 改写多 switch
	//  p.(type)断言
	switch v := p.(type) {
	case int:
		fmt.Println("Integer", v)
	case string:
		fmt.Println("string", v)
	default:
		fmt.Println("Unknow Type")
	}
}

func TestEmptyInterfaceAssert(t *testing.T) {
	DoSomething(11)
	DoSomething("hi")
}
