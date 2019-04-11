package strutstest

import (
	"16_structs/computer"
	"testing"
)

// 创建命名的结构体
// 通过下面代码，我们定义了一个命名的结构体 Employee。
type Employee struct {
	// firstName string
	// lastName  string
	// age       int
	// salary    int
	// 通过把相同类型的字段声明在同一行，结构体可以变得更加紧凑
	firstName, lastName string
	age, salary         int
}

// 创建命名的结构体
func TestCreateNamedStruct(t *testing.T) {
	// 通过指定每个字段名的值，定义了结构体变量 emp1。
	// 字段名的顺序不一定要与声明结构体类型时的顺序相同
	emp1 := Employee{
		firstName: "Sam",
		age:       25,
		salary:    8888,
		lastName:  "Anderson",
	}

	// 省略了字段名。在这种情况下，就需要保证字段名的顺序与声明结构体时的顺序相同。
	emp2 := Employee{"Thomas", "Paul", 29, 7777}

	t.Log("Employee 1", emp1)
	t.Log("Employee 2", emp2)
}

// 创建匿名结构体
func TestAnonymousStruct(t *testing.T) {
	// 定义了一个匿名结构体变量 emp3
	emp3 := struct {
		firstName, lastName string
		age, salary         int
	}{
		firstName: "Andreah",
		lastName:  "Nikola",
		age:       31,
		salary:    5000,
	}

	t.Log("Employee 3", emp3)
}

// 结构体的零值（Zero Value）
func TestZeroValueOfStruct(t *testing.T) {
	// 定义了 emp4，却没有初始化任何值。
	// 因此 firstName 和 lastName 赋值为 string 的零值（""）
	// 而 age 和 salary 赋值为 int 的零值（0）
	var emp4 Employee
	t.Log("Employee 4", emp4)

	// 还可以为某些字段指定初始值，而忽略其他字段
	// 这样，忽略的字段名会赋值为零值
	emp5 := Employee{
		firstName: "John",
		lastName:  "Paul",
	}
	t.Log("Employee 5", emp5)
}

// 访问结构体的字段
// 点号操作符 . 用于访问结构体的字段。
func TestAccessFieldInStruct(t *testing.T) {
	emp6 := Employee{"Sam", "Anderson", 55, 9999}
	t.Log("emp6 FirstName:", emp6.firstName)
	t.Log("emp6 LastName:", emp6.lastName)
	t.Log("emp6 Age:", emp6.age)
	t.Log("emp6 Salary:", emp6.salary)

	// 还可以创建零值的 struct，以后再给各个字段赋值
	var emp7 Employee
	emp7.firstName = "Jack"
	emp7.lastName = "Adams"
	t.Log("Employee 7", emp7)
}

// 结构体的指针
func TestStructPointer(t *testing.T) {
	emp8 := &Employee{"Sam", "Anderson", 55, 6000}

	t.Log("emp8 FirstName", (*emp8).firstName)
	t.Log("emp8 Age", (*emp8).age)

	// Go 语言允许我们在访问 firstName 字段时，
	// 可以使用 emp8.firstName 来代替显式的解引用 (*emp8).firstName。
	t.Log("emp8 FirstName", emp8.firstName)
	t.Log("emp8 Age", emp8.age)
}

// 匿名字段
// 创建结构体时，字段可以只有类型，而没有字段名。这样的字段称为匿名字段（Anonymous Field）。
func TestAnonymousFiled(t *testing.T) {
	// 创建一个 Person 结构体，它含有两个匿名字段 string 和 int。
	type Person struct {
		string
		int
	}

	p := Person{"Naveen", 50}
	t.Log(p)

	//Go 默认这些字段名是它们各自的类型。所以 Person 结构体有两个名为 string 和 int 的字段。
	var p1 Person
	p1.string = "zhangsan"
	p1.int = 55
	t.Log(p1)
}

// 嵌套结构体（Nested Structs）
// 结构体的字段有可能也是一个结构体。这样的结构体称为嵌套结构体
func TestNestedStructs(t *testing.T) {
	type Address struct {
		city, state string
	}

	// 结构体Person里面嵌套了Address结构体
	type Person struct {
		name    string
		age     int
		address Address
	}

	var p Person
	p.name = "Naveen"
	p.age = 50
	p.address = Address{
		city:  "Chiaogo",
		state: "Illionis",
	}
	t.Log("Name:", p.name)
	t.Log("Age:", p.age)
	t.Log("City:", p.address.city)
	t.Log("State:", p.address.state)
}

// 提升字段（Promoted Fields）
// 如果是结构体中有匿名的结构体类型字段，则该匿名结构体里的字段就称为提升字段。
// 这是因为提升字段就像是属于外部结构体一样，可以用外部结构体直接访问
func TestPromotedFields(t *testing.T) {
	type Address struct {
		city, state string
	}
	type Person struct {
		name    string
		age     int
		Address // 匿名的Address结构体，提升字段
	}

	var p Person
	p.name = "Naveen"
	p.age = 50
	p.Address = Address{
		city:  "Chiaogo",
		state: "Illionis",
	}
	// Person 结构体有一个匿名字段 Address，而 Address 是一个结构体。
	// 现在结构体 Address 有 city 和 state 两个字段，
	// 访问这两个字段就像在 Person 里直接声明的一样，因此我们称之为提升字段
	t.Log("Name:", p.name)
	t.Log("Age:", p.age)
	t.Log("City:", p.city)
	t.Log("State:", p.state)
}

// 导出结构体和字段
func TestExported(t *testing.T) {
	var spec computer.Spec
	spec.Maker = "apple"
	spec.Price = 12800

	// 非导出字段不能在包外访问
	// cannot refer to unexported field or method model
	// spec.model = "Mac mini"
	t.Log("Spec:", spec)
}

// 结构体相等性（Structs Equality）
// 结构体是值类型。如果它的每一个字段都是可比较的，则该结构体也是可比较的。
// 如果两个结构体变量的对应字段相等，则这两个变量也是相等的。
func TestStructsEquality(t *testing.T) {
	type name struct {
		firstName string
		lastName  string
	}
	name1 := name{"Steve", "Jobs"}
	name2 := name{"Steve", "Jobs"}
	if name1 == name2 {
		t.Log("name1 and name2 are equal")
	} else {
		t.Log("name1 and name2 are not equal")
	}

	name3 := name{firstName: "Steve", lastName: "Jobs"}
	name4 := name{}
	name4.firstName = "Steve"
	if name3 == name4 {
		t.Log("name3 and name4 are equal")
	} else {
		t.Log("name3 and name4 are not equal")
	}

	// 如果结构体包含不可比较的字段，则结构体变量也不可比较。
	// 结构体类型 image 包含一个 map 类型的字段。
	// 由于 map 类型是不可比较的，因此 image1 和 image2 也不可比较。
	type image struct {
		data map[int]int
	}

	image1 := image{data: map[int]int{0: 155}}
	image2 := image{data: map[int]int{0: 155}}
	t.Log("image1:", image1)
	t.Log("image2:", image2)
	// struct containing map[int]int cannot be compared
	// if image1 == image2 {
	// 	t.Log("image1 and image2 are equal")
	// }
}
