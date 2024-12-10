package solve

import "testing"

func Test10(t *testing.T) {
	tests := []struct {
		input []string
        a1    int
		a2    int
	}{
		{[]string{
			"0123",
			"1234",
			"8765",
			"9876",
		}, 1, 16},
		{[]string{
            "89010123",
            "78121874",
            "87430965",
            "96549874",
            "45678903",
            "32019012",
            "01329801",
            "10456732",
		}, 36, 81},
	}

	for ti, tt := range tests {
		p1, p2, err := Run10(tt.input)
		if err != nil {
			t.Fatalf(err.Error())
		}

		if p1 != tt.a1 {
			t.Errorf("Part %d.1: want %d, got %d", ti, tt.a1, p1)
		}

		if p2 != tt.a2 {
			t.Errorf("Part %d.2: want %d, got %d", ti, tt.a2, p2)
		}
	}
}
