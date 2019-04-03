// switch的执行顺序
// switch的条件从上到下的执行，当匹配成功的时候停止
package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("when's Saturday?")
	today := time.Now().Weekday()
	switch time.Saturday {
	case today + 0:
		fmt.Println("Today.")
	case today + 1:
		fmt.Println("Tomorrow")
	case today + 2:
		fmt.Println("In two days.")
	default:
		fmt.Println("Too far away.")
	}
}
