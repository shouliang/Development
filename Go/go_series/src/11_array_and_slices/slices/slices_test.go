package slicestest

import "testing"

/*
数组，尽管数组看上去似乎足够灵活，但是它们具有固定长度的限制，不可能增加数组的长度。
这就要用到 切片 了。事实上，在 Go 中，切片比传统数组更常见。
切片
切片是由数组建立的一种方便、灵活且功能强大的包装（Wrapper）。
切片本身不拥有任何数据。它们只是对现有数组的引用。
*/

// 创建一个切片
// 带有 T 类型元素的切片由 []T 表示
func TestCreatASlice(t *testing.T) {
	// 创建一个有 3 个整型元素的数组，并返回一个存储在 s1 中的数组的引用。
	s1 := []int{6, 7, 8}
	t.Log(s1)

	// func make（[]T，len，cap）[]T 通过传递类型，长度和容量来创建切片。
	// 容量是可选参数, 默认值为切片长度。make 函数创建一个数组，并返回引用该数组的切片。
	s2 := make([]int, 5, 6)
	t.Log(s2)

	// 使用语法 a[start:end] 创建一个从 a 数组索引 start 开始到 end - 1 结束的切片
	a := [5]int{1, 2, 3, 4, 5}
	var b []int = a[1:4]
	t.Log(b)
	var c = a[0:3]
	t.Log(c)
}

// 切片的修改
// 切片自己不拥有任何数据。它只是底层数组的一种表示。对切片所做的任何修改都会反映在底层数组中。
func TestModifyASlice(t *testing.T) {
	darr := [...]int{57, 89, 90, 82, 100, 78, 67, 69, 59}
	t.Log("arrar before", darr)

	// 根据数组索引 2,3,4 创建一个切片
	dslice := darr[2:5]
	for i := range dslice {
		dslice[i]++
	}

	// 到对切片的更改反映在数组中
	t.Log("arrar after", darr)
}

// 当多个切片共用相同的底层数组时，每个切片所做的更改将反映在数组中。
func TestMultiModifyInASlice(t *testing.T) {
	numa := [3]int{78, 79, 80}
	nums1 := numa[:]
	nums2 := numa[:]
	t.Log("arrary before change 1", numa)
	nums1[0] = 788
	t.Log("arrar after modification to slice nums1", numa)
	nums2[1] = 799
	t.Log("arrar after modification to slice nums2", numa)
	// 从输出中可以清楚地看出，当切片共享同一个数组时，每个所做的修改都会反映在数组中。
}

// 切片的长度和容量
// 切片的长度是切片中的元素数。切片的容量是从创建切片索引开始的底层数组中元素数。
func TestSliceLenAndCapacity(t *testing.T) {
	fruitarray := [...]string{"apple", "orange", "grape", "mango", "watermelon", "pineapple", "chikoo"}
	t.Log("len of array is", len(fruitarray))

	// fruitarray 的长度是 7。fruiteslice 是从 fruitarray 的索引 1 创建的。
	// 所以容量capacity = 7-1 =6,长度len = 3 -1 = 2
	fruitslice := fruitarray[1:3]
	t.Logf("length of slice %d capacity %d", len(fruitslice), cap(fruitslice))

	// 切片可以重置其容量
	fruitslice = fruitslice[:cap(fruitslice)]
	t.Logf("After re-slicing length is %d capacity is %d", len(fruitslice), cap(fruitslice))
}

// 追加切片元素
/*
数组的长度是固定的，它的长度不能增加。 切片是动态的，使用 append 可以将新元素追加到切片上。
append 函数的定义是 func append（s[]T，x ... T）[]T。
x ... T 在函数定义中表示该函数接受参数 x 的个数是可变的。这些类型的函数被称为可变函数。

切片如何具有动态长度。以及内部发生了什么，当新的元素被添加到切片时，会创建一个新的数组。
现有数组的元素被复制到这个新数组中，并返回这个新数组的新切片引用
*/
func TestSliceAppend(t *testing.T) {
	cars := []string{"Ferrari", "Honda", "Ford"}
	t.Log("cars:", cars, "has old length", len(cars), "and capacity", cap(cars))

	cars = append(cars, "Toyota")
	t.Log("cars:", cars, "has new length", len(cars), "and capacity", cap(cars))

	// 切片的零值为nil
	var names []string
	if names == nil {
		t.Log("names == nil")
	}

	// 使用 ... 运算符将一个切片添加到另一个切片
	veggies := []string{"potatoes", "tomatoes", "brinjal"}
	fruits := []string{"oranges", "apples"}
	food := append(veggies, fruits...)
	t.Log("food:", food)
}

// 切片的函数传递
/*
我们可以认为，切片在内部可由一个结构体类型表示。这是它的表现形式，

type slice struct {
    Length        int
    Capacity      int
    ZerothElement *byte
}
切片包含长度、容量和指向数组第零个元素的指针。
当切片传递给函数时，即使它通过值传递，指针变量也将引用相同的底层数组。
因此，当切片作为参数传递给函数时，函数内所做的更改也会在函数外可见
*/
func TestSlicePassToFunction(t *testing.T) {
	numbers := []int{6, 7, 8}
	t.Log("slice before function call", numbers)
	subtactOne(numbers)
	t.Log("slice after function call", numbers)
}

func subtactOne(numbers []int) {
	for i := range numbers {
		numbers[i] -= 2
	}
}

// 多维切片
// 二维切片[][]的形式，其中一维切片的长度可以不一样
func TestMultidimessionSlice(t *testing.T) {
	pls := [][]string{
		{"C", "C++"},
		{"JavaScript"},
		{"GO", "Node.js", "R", "Python"},
	}
	for _, v1 := range pls {
		for _, v2 := range v1 {
			t.Logf("%s ", v2)
		}
		t.Logf("\n")
	}
}

// 内存优化
/*
切片持有对底层数组的引用。只要切片在内存中，数组就不能被垃圾回收。
在内存管理方面，这是需要注意的。
假设我们有一个非常大的数组，我们只想处理它的一小部分。
然后，我们由这个数组创建一个切片，并开始处理切片。这里需要重点注意的是，在切片引用时数组仍然存在内存中。

一种解决方法是使用 copy 函数 func copy(dst，src[]T)int 来生成一个切片的副本。
这样我们可以使用新的切片，原始数组可以被垃圾回收。
*/
func TestSliceCopy(t *testing.T) {
	countries := []string{"China", "USA", "Japan", "Germany", "India", "Australia", "France"}
	neededCountries := countries[:len(countries)-5]

	countriesCpy := make([]string, len(neededCountries))

	// copy后countries 数组可以被垃圾回收, 因为 neededCountries 不再被引用
	copy(countriesCpy, neededCountries)

	t.Log(countriesCpy)
}
