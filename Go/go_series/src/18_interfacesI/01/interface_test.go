package interface01

import "testing"

/* 什么是接口
在面向对象的领域里，接口一般这样定义：接口定义一个对象的行为。
接口只指定了对象应该做什么，至于如何实现这个行为（即实现细节），则由对象本身去确定。

在 Go 语言中，接口就是方法签名（Method Signature）的集合。
当一个类型定义了接口中的所有方法，我们称它实现了该接口。
这与面向对象编程（OOP）的说法很类似。接口指定了一个类型应该具有的方法，并由该类型决定如何实现这些方法。
*/

// 接口的声明与实现

// 创建接口，接口有一个FindVowels() []rune的方法
type VovelsFinder interface {
	FindVowels() []rune
}

// 自定义类型MyString
type MyString string

// 给接受者类型（Receiver Type） MyString 添加了方法 FindVowels() []rune。
// 现在，我们称 MyString 实现了 VowelsFinder 接口
// 无需显式通过implement显式地声明该类实现了接口。
// 而在 Go 中，并不需要这样。如果一个类型包含了接口中声明的所有方法，那么它就隐式地实现了 Go 接口。
func (ms MyString) FindVowels() []rune {
	var vowels []rune
	for _, rune := range ms {
		if rune == 'a' || rune == 'e' || rune == 'i' || rune == 'o' || rune == 'u' {
			vowels = append(vowels, rune)
		}
	}
	return vowels
}

func TestInferfaceDeclare(t *testing.T) {
	name := MyString("Sam Anderson")

	// 声明接口变量v
	var v VovelsFinder

	// 将自定义的MyString类型变量name赋值给接口变量v
	// 由于 MyString 实现了接口中的 VowelFinder方法，因此这是合法的
	v = name

	// 调用了 MyString 类型的 FindVowels 方法
	t.Logf("Vowels are %c", v.FindVowels())
}
