package main

import (
	"testing"
)

func TestBufferChannel(t *testing.T) {
	ch := make(chan string, 2)

	ch <- "aa"
	ch <- "bb"

	t.Log(<-ch)
	t.Log(<-ch)
}
