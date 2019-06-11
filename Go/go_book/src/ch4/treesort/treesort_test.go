package treesort

import (
	"math/rand"
	"sort"
	"testing"
)

func TestTreeSort(t *testing.T) {
	data := make([]int, 50)
	for i := range data {
		data[i] = rand.Int() % 50
	}
	Sort(data)
	if !sort.IntsAreSorted(data) {
		t.Errorf("not sorted: %v", data)
	} else {
		t.Log("data is sorted")
	}
}
