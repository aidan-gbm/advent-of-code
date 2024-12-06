package solve

import "testing"

func Test6(t *testing.T) {
    input := []string{
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    }

	p1, p2, err := Run6(input)
	if err != nil {
		t.Fatalf(err.Error())
	}

	if p1 != 41 {
		t.Errorf("Part 1: want 41, got %d", p1)
	}

	if p2 != 6 {
		t.Errorf("Part 2: want 6, got %d", p2)
	}
}

func Test6Loop(t *testing.T) {
    input := []string{
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#........",
        "........#.",
        "#.........",
        "......#...",
    }

    tests := []struct{
        block position
        loop bool
    }{
        { position{ x: 4, y: 0 }, false },
        { position{ x: 3, y: 6 }, true },
        { position{ x: 6, y: 7 }, true },
    }

    for i, tt := range tests {
        isLoop := checkLoop(input, position{ x: 4, y: 6 }, tt.block)
        if isLoop != tt.loop {
            t.Errorf("Loop check %d expected %v, got %v\n", i, tt.loop, isLoop)
        }
    }
}
