/*defer 的实际应用
当一个函数应该在与当前代码流（Code Flow）无关的环境下调用时，可以使用 defer
*/
package defertest02

import (
	"fmt"
	"sync"
	"testing"
)

type rect struct {
	length int
	width  int
}

// 移除了原先程序中的 3 个 wg.Done 的调用，而是用一个单独的 defer wg.Done() 来取代它。
// 这使得我们的代码更加简洁易懂。

// 此方法中使用 defer 还有一个好处。假设我们使用 if 条件语句，
// 又给 area 方法添加了一条返回路径（Return Path)
func (r rect) area(wg *sync.WaitGroup) {
	defer wg.Done()

	if r.length < 0 {
		fmt.Printf("rect %v's length should be greater than zero\n", r)
		// wg.Done() // 多处添加了wg.Done()
		return
	}

	if r.width < 0 {
		fmt.Printf("rect %v's width should be greater than zero\n", r)
		// wg.Done()
		return
	}

	area := r.length * r.width
	fmt.Printf("rect %v's area %d\n", r, area)
	// wg.Done()
}

func TestDefer(t *testing.T) {
	var wg sync.WaitGroup
	r1 := rect{-67, 89}
	r2 := rect{5, -43}
	r3 := rect{8, 9}
	rects := []rect{r1, r2, r3}
	for _, v := range rects {
		wg.Add(1)
		go v.area(&wg)
	}
	wg.Wait()
	fmt.Println("All go routines finished executing")
}
