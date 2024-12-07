package main

import (
	"aoc2024/solve"
	"fmt"
	"time"
)

var days = map[int]func([]string) (int, int, error){
	1: solve.Run1,
	2: solve.Run2,
	3: solve.Run3,
	4: solve.Run4,
	5: solve.Run5,
	6: solve.Run6,
	7: solve.Run7,
}

func main() {
	for i := range 7 {
		input, err := solve.Load(i + 1)
		if err != nil {
			panic(err.Error())
		}

        start := time.Now()
		p1, p2, err := days[i+1](input)
        elapsed := time.Since(start)
		if err != nil {
			panic(err.Error())
		}

		fmt.Printf("Day %d.1: %d\n", i+1, p1)
		fmt.Printf("Day %d.2: %d\n", i+1, p2)
        fmt.Printf("Day %d time: %s\n", i+1, elapsed)
	}
}
