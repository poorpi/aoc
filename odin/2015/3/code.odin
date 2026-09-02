package aoc

import "core:fmt"
import "../../utils"

TestCase :: struct {
    data: string,
    result: int,
}

Position :: struct {
    x: int,
    y: int,
}

part_1 :: proc(data: string) -> int {
    visited := map[Position]bool{}
    defer delete(visited)
    p := Position{0,0}
    visited[p] = true
    for char in data {
        switch char {
            case '^':
                p.y += 1
            case '>':
                p.x += 1
            case 'v':
                p.y -= 1
            case '<':
                p.x -= 1
        }
        visited[p] = true
	}
    return len(visited)
}

part_2 :: proc(data: string) -> int {
    visited := map[Position]bool{}
    defer delete(visited)
    s := Position{0,0}
    r := Position{0,0}
    visited[s] = true
    visited[r] = true
    for char, index in data {
        p : Position
        if index % 2 == 0 {
            p = s
        } else {
            p = r
        }
        switch char {
            case '^':
                p.y += 1
            case '>':
                p.x += 1
            case 'v':
                p.y -= 1
            case '<':
                p.x -= 1
        }
        visited[p] = true
        if index % 2 == 0 {
            s = p
        } else {
            r = p
        }
	}
    return len(visited)
}

main :: proc() {
    data := utils.get_data(#file)

    // p1
    tests := [?]TestCase{
        TestCase{">", 2},
        TestCase{"^>v<", 4},
        TestCase{"^v^v^v^v^v", 2},
    }
    for test in tests {
        result := part_1(test.data)
        if result != test.result {
            fmt.println("[p1] for", test.data, "expected:", test.result, "got:", result)
            return
        }
    }
    p1 := part_1(data)
    fmt.println("[p1]", p1)

    // p2
    tests2 := [?]TestCase{
        TestCase{"^v", 3},
        TestCase{"^>v<", 3},
        TestCase{"^v^v^v^v^v", 11},
    }
    for test in tests2 {
        result := part_2(test.data)
        if result != test.result {
            fmt.println("[p2] for", test.data, "expected:", test.result, "got:", result)
            return
        }
    }
    p2 := part_2(data)
    fmt.println("[p2]", p2)
}
