package solve

import "testing"

func Test8(t *testing.T) {
	input := []string{
        "............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............",
	}

    a1, a2 := 14, 34
	p1, p2, err := Run8(input)
	if err != nil {
		t.Fatalf(err.Error())
	}

	if p1 != a1 {
		t.Errorf("Part 1: want %d, got %d", a1, p1)
	}

	if p2 != a2 {
		t.Errorf("Part 2: want %d, got %d", a2, p2)
	}
}

func Test8Resonance(t *testing.T) {
    tests := []struct {
        a position
        b position
        res []position
    }{
        {
            position{x: 4, y: 3},
            position{x: 5, y: 5},
            []position{{x: 3, y: 1}, {x: 6, y: 7}},
        },
        {
            position{x: 8, y: 4},
            position{x: 5, y: 5},
            []position{{x: 11, y: 3}, {x: 2, y: 6}},
        },
    }

    for ti, tt := range tests {
        res := calcResonance(tt.a, tt.b)
        if len(res) != len(tt.res) {
            t.Fatalf("resonance test %d expected '%v', got '%v'\n", ti, tt.res, res)
        }

        for ri := range res {
            if res[ri] != tt.res[ri] {
                t.Fatalf("resonance test %d.%d expected '%v', got '%v'\n", ti, ri, tt.res[ri], res[ri])
            }
        }
    }
}
