package solve

import "testing"

func Test7(t *testing.T) {
	input := []string{
		"190: 10 19",
		"3267: 81 40 27",
		"83: 17 5",
		"156: 15 6",
		"7290: 6 8 6 15",
		"161011: 16 10 13",
		"192: 17 8 14",
		"21037: 9 7 18 13",
		"292: 11 6 16 20",
	}

	p1, p2, err := Run7(input)
	if err != nil {
		t.Fatalf(err.Error())
	}

	if p1 != 3749 {
		t.Errorf("Part 1: want 3749, got %d", p1)
	}

	if p2 != 11387 {
		t.Errorf("Part 2: want 11387, got %d", p2)
	}
}

func Test7Perms(t *testing.T) {
	tests := []struct {
		items  []uint8
		length int
		perms  [][]uint8
	}{
		{[]uint8{1, 2}, 1, [][]uint8{
			{1},
			{2},
		}},
		{[]uint8{1, 2}, 2, [][]uint8{
			{1, 1},
			{1, 2},
			{2, 1},
			{2, 2},
		}},
		{[]uint8{1, 2}, 3, [][]uint8{
			{1, 1, 1},
			{1, 1, 2},
			{1, 2, 1},
			{1, 2, 2},
			{2, 1, 1},
			{2, 1, 2},
			{2, 2, 1},
			{2, 2, 2},
		}},
	}

	for ti, tt := range tests {
		perms := permutations(tt.items, tt.length)
		for pi, perm := range perms {
            if len(perm) != len(tt.perms[pi]) {
				t.Fatalf("permutation test %d.%d expected %v, got %v\n", ti, pi, tt.perms[pi], perm)
            }

			for pii, val := range perm {
				if val != tt.perms[pi][pii] {
					t.Errorf("permutation test %d.%d expected %v, got %v\n", ti, pi, tt.perms[pi], perm)
				}
			}
		}
	}
}

func Test7Cat(t *testing.T) {
	tests := []struct {
		ans int64
        items []int64
	}{
        { 12345, []int64{ 12, 345 }},
        { 12, []int64{ 1, 2 }},
        { 156, []int64{ 15, 6 }},
	}

	for ti, tt := range tests {
        if ans := catOp(tt.items[0], tt.items[1]); ans != tt.ans {
            t.Errorf("catOp test %d expected %d, got %d\n", ti, tt.ans, ans)
        }
	}
}
