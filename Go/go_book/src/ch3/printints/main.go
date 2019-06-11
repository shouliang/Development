package main

import (
	"bytes"
	"fmt"
)

func main() {
	fmt.Println(intsToString([]int{2, 1, 3, 5}))
}

func intsToString(values []int) string {
	var buf bytes.Buffer
	buf.WriteByte('[')
	for i, v := range values {
		if i > 0 {
			buf.WriteString(", ")
		}
		fmt.Fprintf(&buf, "%d", v)
	}
	buf.WriteByte(']')
	return buf.String()
}
