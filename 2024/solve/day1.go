package solve

import (
	"slices"
	"strconv"
	"strings"
)

func Run1(input []string) (int, int, error) {
    count := make(map[int]int)
    l := make([]int, len(input))
    r := make([]int, len(input))
    for line := range input {
        res := strings.Split(input[line], "   ")
        num, err := strconv.ParseInt(res[0], 10, 0)
        if err != nil {
            return 0, 0, err
        }

        l[line] = int(num)

        num, err = strconv.ParseInt(res[1], 10, 0)
        if err != nil {
            return 0, 0, err
        }

        r[line] = int(num)

        // Part 2
        if val, ok := count[int(num)]; ok {
            count[int(num)] = val + 1
        } else {
            count[int(num)] = 1
        }
    }

    slices.Sort(l)
    slices.Sort(r)

    sim := 0
    total := 0
    for i := range l {
        if l[i] > r[i] {
            total += l[i] - r[i]
        } else {
            total += r[i] - l[i]
        }

        // Part 2
        if val, ok := count[l[i]]; ok {
            sim += l[i] * val
        }
    }

    return total, sim, nil
}
