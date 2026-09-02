package aoc

import "core:fmt"
import "../../utils"

TestCase :: struct {
    data: string,
    result: int,
}

part_1 :: proc(s: string) -> int {
    floor := 0
    for cp, i in s {
        if cp == '(' {
            floor += 1
        } else if cp == ')' {
            floor -= 1
        } else {
            fmt.println("unknown codepoint:", cp, "at index:", i)
        }
    }
    return floor
}

part_2 :: proc(s: string) -> int {
    floor := 0
    for cp, i in s {
        if cp == '(' {
            floor += 1
        } else if cp == ')' {
            floor -= 1
        } else {
            fmt.println("unknown codepoint:", cp, "at index:", i)
        }
        if floor == -1 {
            return i + 1
        }
    }
    return -1
}

main :: proc() {
    data := utils.get_data(#file)

    // p1
    tests := [?]TestCase{
        TestCase{"(())", 0},
        TestCase{"()()", 0},
        TestCase{"(((", 3},
        TestCase{"(()(()(", 3},
        TestCase{"))(((((", 3},
        TestCase{"())", -1},
        TestCase{"))(", -1},
        TestCase{")))", -3},
        TestCase{")())())", -3},
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
        TestCase{")", 1},
        TestCase{"()())", 5},
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
