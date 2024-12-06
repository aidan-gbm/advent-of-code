package solve

import (
	"bufio"
	"fmt"
	"os"
)

// Direction vector: 0 -> up, 1 -> right, 2 -> down, 3 -> left
type position struct {
    x int
    y int
    dir uint8
}

func Load(day int) ([]string, error) {
	    infile := fmt.Sprintf("input%d.txt", day)
	fd, err := os.Open(infile)
	if err != nil {
		return nil, fmt.Errorf("could not open file: %s", infile)
	}

	lines := make([]string, 0)
	scanner := bufio.NewScanner(fd)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, nil
}

func oob(input []string, pos position) bool {
    if pos.y < 0 || pos.y >= len(input) {
        return true
    } else if pos.x < 0 || pos.x >= len(input[0]) {
        return true
    }

    return false
}
