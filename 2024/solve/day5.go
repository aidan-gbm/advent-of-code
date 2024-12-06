package solve

import (
	"fmt"
	"slices"
	"strconv"
	"strings"
)

func Run5(input []string) (int, int, error) {
    rules, line, err := loadRules(input)
    if err != nil {
        return 0, 0, err
    }

    updates := make([][]uint8, len(input) - line)

    for i := line; i < len(input); i++ {
        nums := strings.Split(input[i], ",")
        update := make([]uint8, 0, len(nums))
        for _, num := range nums {
            if pageval, err := strconv.ParseUint(num, 10, 8); err != nil {
                return 0, 0, err
            } else {
                update = append(update, uint8(pageval))
            }
        }

        updates[i - line] = update
    }

    sortUpdate := func(a, b uint8) int {
        if prereqs, ok := rules[a]; ok {
            for _, req := range prereqs {
                if req == b {
                    return -1
                }
            }
        }

        if prereqs, ok := rules[b]; ok {
            for _, req := range prereqs {
                if req == a {
                    return 1
                }
            }
        }

        return 0
    }

    valid := make([][]uint8, 0, len(updates))
    invalid := make([][]uint8, 0, len(updates))
    for _, update := range updates {
        if followsRules(update, rules) {
            valid = append(valid, update)
        } else {
            slices.SortFunc(update, sortUpdate)
            invalid = append(invalid, update)
        }
    }

    var p1, p2 int
    for _, update := range valid {
        mid := len(update) / 2
        p1 += int(update[mid])
    }

    for _, update := range invalid {
        mid := len(update) / 2
        p2 += int(update[mid])
    }

	return p1, p2, nil
}

func followsRules(update []uint8, rules map[uint8][]uint8) bool {
    for pageIdx, page := range update {
        if prereqs, ok := rules[page]; ok {
            for _, req := range prereqs {
                reqIdx := slices.Index(update, req)
                if reqIdx >= 0 && reqIdx > pageIdx {
                    return false
                }
            }
        }
    }

    return true
}

func loadRules(input []string) (map[uint8][]uint8, int, error) {
    rules := make(map[uint8][]uint8, 0)

    var line int
    for line = range input {
        if input[line] == "" {
            break
        }

        nums := strings.Split(input[line], "|")
        if len(nums) != 2 {
            return nil, 0, fmt.Errorf("bad input on line %d", line)
        }

        var num1, num2 uint8
        if num, err := strconv.ParseUint(nums[0], 10, 8); err != nil {
            return nil, 0, err
        } else {
            num1 = uint8(num)
        }

        if num, err := strconv.ParseUint(nums[1], 10, 8); err != nil {
            return nil, 0, err
        } else {
            num2 = uint8(num)
        }

        if prereqs, ok := rules[num2]; ok {
            rules[num2] = append(prereqs, num1)
        } else {
            rules[num2] = []uint8{ num1 }
        }
    }

    return rules, line + 1, nil
}
