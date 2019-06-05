package main

import (
	"strings"
	"testing"
)

func BenchmarkStringPlus(b *testing.B) {
	for i := 0; i < b.N; i++ {
		var s, sep string
		for _, str := range []string{"aaa", "bbb", "ccc"} {
			s += sep + str
			sep = " "
		}
	}
}
func BenchmarkStringJoin(b *testing.B) {
	for i := 0; i < b.N; i++ {
		strings.Join([]string{"aaa", "bbb", "ccc"}, " ")
	}
}
