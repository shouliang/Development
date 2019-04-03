// nil slice
package main

import "fmt"

func main() {
	var z []int
	fmt.Println(z, len(z), cap(z))

	// slice的零值是nil
	if z == nil {
		fmt.Println("nil!")
	}
}
