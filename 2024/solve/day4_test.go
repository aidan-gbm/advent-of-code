package solve

import "testing"

func Test4(t *testing.T) {
    input := []string{
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    }

	p1, p2, err := Run4(input)
	if err != nil {
		t.Fatalf(err.Error())
	}

	if p1 != 18 {
		t.Logf("Part 1: want 18, got %d", p1)
		t.Fail()
	}

	if p2 != 9 {
		t.Logf("Part 2: want 9, got %d", p2)
		t.Fail()
	}
}
