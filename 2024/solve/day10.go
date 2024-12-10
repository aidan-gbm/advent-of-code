package solve

func Run10(input []string) (int, int, error) {
    var p1, p2 int
    for y, line := range input {
        for x := range line {
            if input[y][x] == '0' {
                start := position{x: x, y: y}
                ends := trailEnds(input, start)
                p1 += len(ends)
                p2 += trailRating(input, start)
            }
        }
    }

    return p1, p2, nil
}

func trailEnds(input []string, start position) map[position]bool {
    elevation := int(input[start.y][start.x] - byte('0'))
    if elevation == 9 {
        return map[position]bool{
            start: true,
        }
    }

    ends := map[position]bool{}
    next := []position{
        {x: start.x, y: start.y - 1},
        {x: start.x + 1, y: start.y},
        {x: start.x, y: start.y + 1},
        {x: start.x - 1, y: start.y},
    }

    for _, pos := range next {
        if oob(input, pos) {
            continue
        }

        nextElev := int(input[pos.y][pos.x] - byte('0'))
        if nextElev - elevation == 1 {
            for end := range trailEnds(input, pos) {
                ends[end] = true
            }
        }
    }

    return ends
}

func trailRating(input []string, start position) int {
    elevation := int(input[start.y][start.x] - byte('0'))
    if elevation == 9 {
        return 1
    }

    var rating int
    next := []position{
        {x: start.x, y: start.y - 1},
        {x: start.x + 1, y: start.y},
        {x: start.x, y: start.y + 1},
        {x: start.x - 1, y: start.y},
    }

    for _, pos := range next {
        if oob(input, pos) {
            continue
        }

        nextElev := int(input[pos.y][pos.x] - byte('0'))
        if nextElev - elevation == 1 {
            rating += trailRating(input, pos)
        }
    }

    return rating
}
