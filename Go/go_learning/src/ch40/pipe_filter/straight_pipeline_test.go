package pipefilter

import "testing"

func TestStraightPipeline(t *testing.T) {
	spliter := NewSplitFilter(",")
	converter := NewToIntFilter()
	sum := NewSumFilter()

	sp := NewStraightPipeline("P1", spliter, converter, sum)
	ret, err := sp.Process("1,2,3")
	if err != nil {
		t.Fatal(err)
	}
	if ret != 6 {
		t.Fatalf("The expected is 6, but the actual is %d", ret)
	} else {
		t.Log("sum is", ret)
	}

}
