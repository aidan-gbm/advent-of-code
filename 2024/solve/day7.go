package solve

import (
	"math"
	"strconv"
	"strings"
)

func Run7(input []string) (int, int, error) {
    var p1, p2 int
	for _, line := range input {
		parts := strings.Split(line, ": ")
		numsRaw := strings.Split(parts[1], " ")

        total, err := strconv.ParseInt(parts[0], 10, 0)
        if err != nil {
            return 0, 0, nil
        }

        nums := make([]int64, 0, len(numsRaw))
        for _, nr := range numsRaw {
            n, err := strconv.ParseInt(nr, 10, 0)
            if err != nil {
                return 0, 0, err
            }

            nums = append(nums, n)
        }

        if calibrate(nums, total, false) {
            p1 += int(total)
            p2 += int(total)
        } else if calibrate(nums, total, true) {
            p2 += int(total)
        }
	}

	return p1, p2, nil
}

func calibrate(nums []int64, total int64, cat bool) bool {
    if len(nums) == 1 {
        return nums[0] == total
    } else if nums[0] > total {
        return false
    }

    newNums := make([]int64, 0, len(nums) - 1)

    // Try: add
    next := nums[0] + nums[1]
    newNums = append(newNums, next)
    newNums = append(newNums, nums[2:]...)
    if calibrate(newNums, total, cat) {
        return true
    }
    newNums = newNums[:0]

    // Try: multiply
    next = nums[0] * nums[1]
    newNums = append(newNums, next)
    newNums = append(newNums, nums[2:]...)
    if calibrate(newNums, total, cat) {
        return true
    }
    newNums = newNums[:0]

    // Try: concatenate
    if !cat {
        return false
    } else {
        next = catOp(nums[0], nums[1])
        newNums = append(newNums, next)
        newNums = append(newNums, nums[2:]...)
        return calibrate(newNums, total, cat)
    }
}

func catOp(a, b int64) int64 {
    var digits int
    for n := b; n > 0; n = n / 10 {
        digits++
    }

    return a * int64(math.Pow10(digits)) + b
}
