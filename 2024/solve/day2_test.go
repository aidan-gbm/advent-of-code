package solve

import "testing"

func Test2(t *testing.T) {
    input := []string{
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    }

	p1, p2, err := Run2(input)
	if err != nil {
		t.Fatalf(err.Error())
	}

	if p1 != 2 {
		t.Logf("Part 1: want 2, got %d", p1)
		t.Fail()
	}

	if p2 != 4 {
		t.Logf("Part 2: want 4, got %d", p2)
		t.Fail()
	}
}
