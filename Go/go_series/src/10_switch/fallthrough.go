// 在 Go 中，每执行完一个 case 后，会从 switch 语句中跳出来，不再做后续 case 的判断和执行。
// 使用 fallthrough 语句可以在已经执行完成的 case 之后，把控制权转移到下一个 case 的执行代码中。
package main
import "fmt"

func number() int {
	num := 15 * 5
	return num
}

func main() {
	switch num := number(); {
  case num < 50:
    fmt.Printf("%d is lesser than 50\n",num)
    fallthrough
  case num < 100:
    fmt.Printf("%d is lesser than 100\n",num)
    fallthrough
  case num < 200:
    fmt.Printf("%d is lesser than 200\n",num)
	}
}
