package solve

import (
	"math"
	"strconv"
	"strings"
)

type p7op func(a, b int64) int64

func Run7(input []string) (int, int, error) {
    var p1, p2 int
	for _, line := range input {
		parts := strings.Split(line, ": ")
		nums := strings.Split(parts[1], " ")

        ops1 := permutations([]p7op{addOp, mulOp}, len(nums) - 1)
        for _, ops := range ops1 {
            total, err := strconv.ParseInt(parts[0], 0, 0)
            if err != nil {
                return 0, 0, err
            }

            var acc int64
            for i, num := range nums {
                n, err := strconv.ParseInt(num, 0, 0)
                if err != nil {
                    return 0, 0, err
                }

                if i == 0 {
                    acc = n
                } else {
                    acc = ops[i-1](acc, n)
                }
            }

            if total == acc {
                p1 += int(total)
                break
            } else if total < acc {
                break
            }
        }

        ops2 := permutations([]p7op{addOp, mulOp, catOp}, len(nums) - 1)
        for _, ops := range ops2 {
            total, err := strconv.ParseInt(parts[0], 0, 0)
            if err != nil {
                return 0, 0, err
            }

            var acc int64
            for i, num := range nums {
                n, err := strconv.ParseInt(num, 0, 0)
                if err != nil {
                    return 0, 0, err
                }

                if i == 0 {
                    acc = n
                } else {
                    acc = ops[i-1](acc, n)
                }
            }

            if total == acc {
                p2 += int(total)
                break
            } else if total < acc {
                break
            }

        }
	}

	return p1, p2, nil
}

func addOp(a, b int64) int64 {
	return a + b
}

func mulOp(a, b int64) int64 {
	return a * b
}

func catOp(a, b int64) int64 {
    var digits int
    for n := b; n > 0; n = n / 10 {
        digits++
    }

    return a * int64(math.Pow10(digits)) + b
}

func permutations[T any](items []T, length int) [][]T {
	perms := make([][]T, 0, int(math.Pow(float64(len(items)), float64(length))))
    if length == 1 {
        for _, item := range items {
            perms = append(perms, []T{item})
        }

        return perms
    }

    for _, item := range items {
        for _, sub := range permutations(items, length - 1) {
            perms = append(perms, append([]T{item}, sub...))
        }
    }

    return perms
}
