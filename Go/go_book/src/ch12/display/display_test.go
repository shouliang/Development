package display

import "testing"

func Test_slice(t *testing.T) {
	Display("slice", []*int{new(int), nil})
}
