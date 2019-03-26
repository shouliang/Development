// 展示无法从另外一个包里访问未公开的标识符
package main

import (
	"chapter5/listing64/counters"
	"fmt"
)

func main() {
	// 不能引用为公开的成员
	counter := counters.alterCounter(10)

	fmt.Printf("Counter: %d\n", counter)
}
