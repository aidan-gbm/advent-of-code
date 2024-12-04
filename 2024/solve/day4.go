package solve

type position struct {
    x int
    y int
}

func Run4(input []string) (int, int, error) {
    var totalA, totalB int
    for y := range input {
        for x := range input[y] {
            for dir := range 8 {
                if findXmas(input, x, y, dir) {
                    totalA += 1
                }

            }

            if input[y][x] == 'A' && findMas(input, x, y) {
                totalB += 1
            }
        }
    }

	return totalA, totalB, nil
}

func findXmas(input []string, startX, startY, dir int) bool {
	pos := position {
		x: startX,
		y: startY,
	}

	for _, chr := range []byte("XMAS") {
		if oob(input, pos.x, pos.y) {
            return false
        } else if input[pos.y][pos.x] != chr {
			return false
		}

		switch dir {
		case 0: // E
			pos.x += 1
		case 1: // SE
			pos.x += 1
			pos.y += 1
		case 2: // S
			pos.y += 1
		case 3: // SW
			pos.x -= 1
			pos.y += 1
		case 4: // W
			pos.x -= 1
		case 5: // NW
			pos.x -= 1
			pos.y -= 1
		case 6: // N
			pos.y -= 1
		case 7: // NE
			pos.x += 1
			pos.y -= 1
		}
	}

	return true
}

func findMas(input []string, startX, startY int) bool {
    var next byte
    coords := [4]position{
        { startX - 1, startY - 1}, { startX + 1, startY + 1 },
        { startX - 1, startY + 1}, { startX + 1, startY - 1 },
    }

    for _, loc := range coords {
        if oob(input, loc.x, loc.y) {
            return false
        }
    }

    if input[coords[0].y][coords[0].x] == 'M' {
        next = 'S'
    } else if input[coords[0].y][coords[0].x] == 'S' {
        next = 'M'
    } else {
        return false
    }

    if input[coords[1].y][coords[1].x] != next {
        return false
    }

    if input[coords[2].y][coords[2].x] == 'M' {
        next = 'S'
    } else if input[coords[2].y][coords[2].x] == 'S' {
        next = 'M'
    } else {
        return false
    }

    if input[coords[3].y][coords[3].x] != next {
        return false
    }

    return true
}

func oob(input []string, x, y int) bool {
    if y < 0 || y >= len(input) {
        return true
    } else if x < 0 || x >= len(input[0]) {
        return true
    }

    return false
}
