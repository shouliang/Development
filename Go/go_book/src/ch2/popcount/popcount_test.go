package popcount

import "testing"

func TestPopCount(t *testing.T) {
	i := PopCount(uint64(17))
	t.Log(i)
}
