// 没有条件的switch
// 没有条件的switch 同 switch true一样
// 这一构造使得可以用更清晰的形式来编写长的 if-then-else链
package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon")
	default:
		fmt.Println("Good evening")
	}
}
