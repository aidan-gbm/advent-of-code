package main

import (
	"aoc2024/solve"
	"flag"
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
	8: solve.Run8,
}

func main() {
    var day int
    var all bool
    flag.BoolVar(&all, "a", false, "run all days")
    flag.IntVar(&day, "d", 0, "the day to run")
    flag.Parse()

    if all {
        for di := range days {
            run(di)
        }
    } else if day == 0 {
        flag.Usage()
    } else if day > len(days) {
        fmt.Println("invalid day")
    } else {
        run(day)
    }
}

func run(day int) {
    input, err := solve.Load(day)
    if err != nil {
        panic(err.Error())
    }

    start := time.Now()
    p1, p2, err := days[day](input)
    elapsed := time.Since(start)
    if err != nil {
        panic(err.Error())
    }

    fmt.Printf("Day %d.1: %d\n", day, p1)
    fmt.Printf("Day %d.2: %d\n", day, p2)
    fmt.Printf("Day %d time: %s\n", day, elapsed)
}
