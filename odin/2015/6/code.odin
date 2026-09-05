package aoc

import "core:fmt"
import "core:strconv"
import "core:strings"
import "../../utils"

TestCase :: struct {
    data: string,
    result: int,
}

Operation :: enum{Toggle, On, Off}

Point :: struct {
    x: int,
    y: int,
}

parse_point :: proc(data: string) -> Point {
    parts := strings.split(data, ",")
    x, _ := strconv.parse_int(parts[0])
    y, _ := strconv.parse_int(parts[1])
    return Point{x, y}
}

parse_line :: proc(line: string) -> (Operation, Point, Point) {
    parts := strings.split(line, " ")
    operation : Operation
    p1 : Point
    p2 : Point
    if parts[0] == "toggle" {
        operation = Operation.Toggle
        p1 = parse_point(parts[1])
        p2 = parse_point(parts[3])
    } else if parts[1] == "on" {
        operation = Operation.On
        p1 = parse_point(parts[2])
        p2 = parse_point(parts[4])
    } else {
        operation = Operation.Off
        p1 = parse_point(parts[2])
        p2 = parse_point(parts[4])
    }
    if p1.x < p2.x || p1.y < p2.y {
        return operation, p1, p2
    } else {
        return operation, p2, p1
    }
}

part_1 :: proc(data: string) -> int {
    lit_count := 0
    lights := new([1_000][1_000]bool)
    defer free(lights)
    for line in strings.split_lines(data) {
        operation, top_left, bottom_right := parse_line(line)
        for xx := top_left.x; xx <= bottom_right.x; xx += 1 {
            for yy := top_left.y; yy <= bottom_right.y; yy += 1 {
                previous_value := lights[xx][yy]
                new_value : bool
                switch operation {
                    case Operation.Toggle:
                        new_value = !previous_value
                    case Operation.On:
                        new_value = true
                    case Operation.Off:
                        new_value = false
                }
                lights[xx][yy] = new_value
                if previous_value == new_value {
                    continue
                } else if previous_value {
                    lit_count -= 1
                } else {
                    lit_count += 1
                }
            }
        }
    }
    return lit_count
}

part_2 :: proc(data: string) -> int {
    total_brightness := 0
    lights := new([1_000][1_000]int)
    defer free(lights)
    for line in strings.split_lines(data) {
        operation, top_left, bottom_right := parse_line(line)
        for xx := top_left.x; xx <= bottom_right.x; xx += 1 {
            for yy := top_left.y; yy <= bottom_right.y; yy += 1 {
                previous_value := lights[xx][yy]
                new_value : int
                switch operation {
                    case Operation.Toggle:
                        new_value = previous_value + 2
                    case Operation.On:
                        new_value = previous_value + 1
                    case Operation.Off:
                        new_value = previous_value - 1
                        if new_value < 0 {
                            new_value = 0
                        }
                }
                lights[xx][yy] = new_value
                total_brightness += new_value - previous_value
            }
        }
    }
    return total_brightness
}

main :: proc() {
    data := utils.get_data(#file)

    // p1
    tests := [?]TestCase{
        TestCase{"turn on 0,0 through 999,999", 1_000_000},
        TestCase{"toggle 0,0 through 999,0", 1_000},
        TestCase{"turn on 0,0 through 999,999\nturn off 499,499 through 500,500", 999_996},
        TestCase{"turn on 0,0 through 999,999\nturn off 499,499 through 500,500\ntoggle 0,0 through 999,0", 998_996},
        TestCase{"turn on 0,0 through 999,999\nturn off 499,499 through 500,500\nturn on 0,0 through 999,999", 1_000_000},
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
        TestCase{"turn on 0,0 through 0,0", 1},
        TestCase{"toggle 0,0 through 999,999", 2_000_000},
        TestCase{"turn off 0,0 through 999,999", 0},
        TestCase{"turn on 0,0 through 999,999\nturn off 0,0 through 999,999", 0},
        TestCase{"toggle 0,0 through 999,999\nturn off 0,0 through 999,999", 1_000_000},
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
