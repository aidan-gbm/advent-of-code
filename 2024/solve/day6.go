package solve

func Run6(input []string) (int, int, error) {
    guard := findAndReplace(input, '^', '.')
    p1, visited := countPositions(input, guard)

    var p2 int
    for y := range visited {
        for x := range visited[y] {
            if visited[y][x] && checkLoop(input, guard, position{ x: x, y: y }) {
                p2++
            }
        }
    }

	return p1, p2, nil
}

func countPositions(input []string, pos position) (int, [][]bool) {
    visited := make([][]bool, len(input))
    for row := range visited {
        visited[row] = make([]bool, len(input[row]))
    }

    count := 1
    visited[pos.y][pos.x] = true

    for true {
        var oob bool
        if pos, oob = move(input, pos); oob {
            break
        } else if !visited[pos.y][pos.x] {
            visited[pos.y][pos.x] = true
            count++
        }
    }

    return count, visited
}

func checkLoop(input []string, start position, block position) bool {
    obstacles := make(map[position]bool, 0)

    area := make([]string, len(input))
    copy(area, input)
    area[block.y] = area[block.y][:block.x] + "#" + area[block.y][block.x+1:]

    pos := start
    for true {
        var oob bool
        prevDir := pos.dir
        if pos, oob = move(area, pos); oob {
            break
        }

        var oPos position
        if prevDir != pos.dir {
            switch prevDir {
            case 0:
                oPos = position{ x: pos.x, y: pos.y - 1, dir: prevDir }
            case 1:
                oPos = position{ x: pos.x + 1, y: pos.y, dir: prevDir }
            case 2:
                oPos = position{ x: pos.x, y: pos.y + 1, dir: prevDir }
            case 3:
                oPos = position{ x: pos.x - 1, y: pos.y, dir: prevDir }
            }

            if _, ok := obstacles[oPos]; ok {
                return true
            } else {
                obstacles[oPos] = true
            }
        }
    }

    return false
}

// Moves the position (or turns) by 1 and returns OOB status
func move(input []string, pos position) (position, bool) {
    var next position
    switch pos.dir {
    case 0:
        next = position{ x: pos.x, y: pos.y - 1, dir: pos.dir }
    case 1:
        next = position{ x: pos.x + 1, y: pos.y, dir: pos.dir }
    case 2:
        next = position{ x: pos.x, y: pos.y + 1, dir: pos.dir }
    case 3:
        next = position{ x: pos.x - 1, y: pos.y, dir: pos.dir }
    }

    if oob(input, next) {
        return next, true
    } else if input[next.y][next.x] == '#' {
        pos.dir = (pos.dir + 1) % 4
    } else if input[next.y][next.x] == '.' {
        pos = next
    }

    return pos, false
}

func findAndReplace(input []string, find rune, repl rune) position {
    for y, row := range input {
        for x, chr := range row {
            if chr == find {
                input[y] = input[y][:x] + string(repl) + input[y][x+1:]
                return position{x: x, y: y, dir: 0}
            }
        }
    }

    return position{}
}
