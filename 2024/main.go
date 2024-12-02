package main

import (
	"aoc2024/solve"
	"fmt"
)

var days = map[int]func([]string) (int, int, error){
	1: solve.Run1,
	2: solve.Run2,
}

func main() {
	for i := range 2 {
		input, err := solve.Load(i + 1)
		if err != nil {
			panic(err.Error())
		}
		p1, p2, err := days[i+1](input)
		if err != nil {
			panic(err.Error())
		}

		fmt.Printf("Day %d.1: %d\n", i+1, p1)
		fmt.Printf("Day %d.2: %d\n", i+1, p2)
	}
}
