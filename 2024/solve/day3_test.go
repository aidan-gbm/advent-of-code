package solve

import "testing"

func Test3a(t *testing.T) {
    input := []string{
        "mul(44,46)",
    }

	p1, p2, err := Run3(input)
	if err != nil {
		t.Fatalf(err.Error())
	}

	if p1 != 2024 {
		t.Logf("Part 1: want 2024, got %d", p1)
		t.Fail()
	}

	if p2 != 2024 {
		t.Logf("Part 2: want 2024, got %d", p2)
		t.Fail()
	}
}

func Test3b(t *testing.T) {
    input := []string{
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
    }

	p1, p2, err := Run3(input)
	if err != nil {
		t.Fatalf(err.Error())
	}

	if p1 != 161 {
		t.Logf("Part 1: want 161, got %d", p1)
		t.Fail()
	}

	if p2 != 161 {
		t.Logf("Part 2: want 161, got %d", p2)
		t.Fail()
	}
}

func Test3c(t *testing.T) {
    input := []string{
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
    }

	p1, p2, err := Run3(input)
	if err != nil {
		t.Fatalf(err.Error())
	}

	if p1 != 161 {
		t.Logf("Part 1: want 161, got %d", p1)
		t.Fail()
	}

	if p2 != 48 {
		t.Logf("Part 2: want 48, got %d", p2)
		t.Fail()
	}
}
