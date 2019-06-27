package methods_test

import (
	"ch12/methods"
	"strings"
	"testing"
	"time"
)

func Test(t *testing.T) {
	methods.Print(time.Hour)

	methods.Print(new(strings.Replacer))
}
