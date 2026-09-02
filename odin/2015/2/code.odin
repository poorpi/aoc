package aoc

import "core:fmt"
import "core:strings"
import "core:strconv"
import "../../utils"

TestCase :: struct {
    data: string,
    result: int,
}

parse_line :: proc(line: string) -> (int, int, int) {
    dim, de :=  strings.split(line, "x")
    w, we := strconv.parse_int(dim[0])
    h, he := strconv.parse_int(dim[1])
    l, le := strconv.parse_int(dim[2])
    return w, h, l
}

surface_area :: proc(area_a: int, area_b: int, area_c: int) -> int {
    return 2 * area_a + 2 * area_b + 2 * area_c
}

area :: proc(a: int, b: int) -> int {
    return a * b
}

part_1 :: proc(s: string) -> int {
    result : int
    for line in strings.split_lines(s) {
        w, h, l := parse_line(line)
        area_a := area(w, h)
        area_b := area(h, l)
        area_c := area(l, w)
        result += surface_area(area_a, area_b, area_c)
        result += min(area_a, area_b, area_c)
	}
    return result
}

volume :: proc(w: int, h: int, l: int) -> int {
    return w * h * l
}

perimiter :: proc(a: int, b: int) -> int {
    return 2 * a + 2 * b
}

part_2 :: proc(s: string) -> int {
    result : int
    for line in strings.split_lines(s) {
        w, h, l := parse_line(line)
        p1 := perimiter(w, h)
        p2 := perimiter(h, l)
        p3 := perimiter(l, w)
        result += min(p1, p2, p3)
        result += volume(w, h, l)
	}
    return result
}

main :: proc() {
    data := utils.get_data(#file)

    // p1
    tests := [?]TestCase{
        TestCase{"2x3x4", 58},
        TestCase{"1x1x10", 43},
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
        TestCase{"2x3x4", 34},
        TestCase{"1x1x10", 14},
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
