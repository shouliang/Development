package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println(os.Args[0])

	for index, arg := range os.Args {
		fmt.Println(index, arg)
	}
}
