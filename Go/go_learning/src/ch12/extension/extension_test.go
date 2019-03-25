// 继承：Go实际是不支持继续的
package extension

import (
	"fmt"
	"testing"
)

type Pet struct {
}

func (p *Pet) Speak() {
	fmt.Print("...")
}

func (p *Pet) SpeakTo(host string) {
	// 可以调用之前定义的方法
	p.Speak()
	fmt.Println(" ", host)
}

//----------- define Dog -----------

type Dog struct {
	// 嵌入了*Pet  匿名嵌套类型
	Pet
}

// func (d *Dog) Speak() {
// 	fmt.Println("Wang!")
// }

// 自定义方法会覆盖掉嵌套类型中的同名方法
func (d *Dog) SpeakTo(host string) {
	d.Speak()
	fmt.Println(" ", host)
}

func TestDog(t *testing.T) {
	//var dog Dog
	dog := new(Dog)

	// cannot use new(Dog) (type *Dog) as type Pet in assignment 不支持从Dog类型向Pet转换
	//var dog Pet = new(Dog)
	// dog.Speak()
	dog.SpeakTo("Cai")
}
