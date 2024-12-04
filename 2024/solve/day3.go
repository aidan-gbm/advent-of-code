package solve

import (
	"regexp"
	"strconv"
)

func Run3(input []string) (int, int, error) {
	re := regexp.MustCompile(`(mul\((?P<a>\d+),(?P<b>\d+)\))|(?P<on>do\(\))|(?P<off>don't\(\))`)
	subOff := re.SubexpIndex("off")
	subOn := re.SubexpIndex("on")
	subA := re.SubexpIndex("a")
	subB := re.SubexpIndex("b")

	var enabled = true
	var totalA, totalB int
	for line := range input {
		matches := re.FindAllStringSubmatch(input[line], -1)
		for match := range matches {
			if matches[match][subOn] != "" {
				enabled = true
				continue
			} else if matches[match][subOff] != "" {
				enabled = false
				continue
			}

			a, err := strconv.ParseInt(matches[match][subA], 10, 0)
			if err != nil {
				return 0, 0, err
			}

			b, err := strconv.ParseInt(matches[match][subB], 10, 0)
			if err != nil {
				return 0, 0, err
			}

			totalA += int(a * b)
			if enabled {
				totalB += int(a * b)
			}
		}
	}
	return totalA, totalB, nil
}
