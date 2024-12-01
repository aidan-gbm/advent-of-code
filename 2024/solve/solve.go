package solve

import (
	"bufio"
	"fmt"
	"os"
)

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
