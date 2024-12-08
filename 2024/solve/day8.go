package solve

type resonance struct {
    pos position
    freq rune
}

func Run8(input []string) (int, int, error) {
    var freqs []rune
    var antennas = make(map[rune][]position)
    var antinodes = make(map[position]bool)
    var antinodes2 = make(map[position]bool)

    for y, line := range input {
        for x, chr := range line {
            if chr != '.' {
                if grp, ok := antennas[chr]; ok {
                    grp = append(grp, position{x: x, y: y})
                    antennas[chr] = grp
                    freqs = append(freqs, chr)
                } else {
                    antennas[chr] = make([]position, 1)
                    antennas[chr][0].x = x
                    antennas[chr][0].y = y
                }
            }
        }
    }

    for _, nodes := range antennas {
        for a := range nodes {
            for b := a + 1; b < len(nodes); b++ {
                for _, res := range calcResonance(nodes[a], nodes[b]) {
                    if !oob(input, res) {
                        antinodes[res] = true
                    }
                }
            }
        }
    }

    for _, nodes := range antennas {
        for a := range nodes {
            for b := a + 1; b < len(nodes); b++ {
                for _, res := range calcResonance2(input, nodes[a], nodes[b]) {
                    if !oob(input, res) {
                        antinodes2[res] = true
                    }
                }
            }
        }
    }

    return len(antinodes), len(antinodes2), nil
}

func calcResonance(a, b position) []position {
    anodes := make([]position, 0, 2)
    diff := position{x: b.x - a.x, y: b.y - a.y}
    return append(
        anodes,
        position{x: a.x - diff.x, y: a.y - diff.y},
        position{x: b.x + diff.x, y: b.y + diff.y},
    )
}

func calcResonance2(input []string, a, b position) []position {
    anodes := make([]position, 0)
    diff := position{x: b.x - a.x, y: b.y - a.y}

    var i int
    test := position{x: a.x, y: a.y}
    for !oob(input, test) {
        i++
        anodes = append(anodes, test)
        test = position{x: a.x - diff.x * i, y: a.y - diff.y * i}
    }

    i = 0
    test = position{x: b.x, y: b.y}
    for !oob(input, test) {
        i++
        anodes = append(anodes, test)
        test = position{x: b.x + diff.x * i, y: b.y + diff.y * i}
    }

    return anodes
}
