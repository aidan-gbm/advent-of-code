package solve

import (
	"testing"
)

func Test1(t *testing.T) {
    input := []string{
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    }

    p1, p2, err := Run1(input)
    if err != nil {
        t.Fatalf(err.Error())
    }

    if p1 != 11 {
        t.Logf("Part 1: want 11, got %d", p1)
        t.Fail()
    }

    if p2 != 31 {
        t.Logf("Part 2: want 31, got %d", p2)
        t.Fail()
    }
}
