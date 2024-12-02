package solve

import (
	"strconv"
	"strings"
)

func Run2(input []string) (int, int, error) {
    var safe = 0
    var semiSafe = 0
    for report := range input {
        levels := strings.Fields(input[report])
        if ok, err := isSafe(levels); err != nil {
            return 0, 0, err
        } else if ok {
            semiSafe += 1
            safe += 1
            continue
        }

        removed := make([]string, len(levels))
        for level := range levels {
            copy(removed, levels)
            removed := append(removed[:level], removed[level+1:]...)
            if ok, err := isSafe(removed); err != nil {
                return 0, 0, err
            } else if ok {
                semiSafe += 1
                break
            }
        }
    }

    return safe, semiSafe, nil
}

func isSafe(level []string) (bool, error) {
    var diff, last int
    var increasing bool
    for idx := range level {
        num, err := strconv.ParseInt(level[idx], 10, 0)
        if err != nil {
            return false, err
        } else if idx == 0 {
            last = int(num)
            continue
        } else if idx == 1 {
            increasing = last < int(num)
        }

        if increasing {
            diff = int(num) - last
        } else {
            diff = last - int(num)
        }

        if ! (diff >= 1 && diff <= 3) {
            return false, nil
        }

        last = int(num)
    }

    return true, nil
}
