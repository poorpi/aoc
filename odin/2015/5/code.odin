package aoc

import "core:fmt"
import "core:math"
import "core:strings"
import "../../utils"

TestCase :: struct {
    data: string,
    result: int,
}

part_1 :: proc(data: string) -> int {
    nice_count := 0
    vowels := [?]rune{'a', 'e', 'i', 'o', 'u'}
    forbidden := [?]string{"ab", "cd", "pq", "xy"}
    for line in strings.split_lines(data) {
        vowel_count := 0
        double_check := false
        forbidden_check := true
        prev : rune
        for ch, i in line {
            for v in vowels {
                if ch == v {
                    vowel_count += 1
                    break
                }
            }
            if i > 0 {
                if prev == ch {
                    double_check = true
                }
                for f in forbidden {
                    if line[i-1:i+1] == f {
                        forbidden_check = false
                    }
                }
            }
            prev = ch
        }
        if vowel_count >= 3 && double_check && forbidden_check{
            nice_count += 1
        }
    }
    return nice_count
}

part_2 :: proc(data: string) -> int {
    nice_count := 0
    for line in strings.split_lines(data) {
        triplets_check := false
        doubles := map[string][dynamic]int{}
        defer {
            for _, dynamic_array in doubles {
                delete(dynamic_array)
            }
            delete(doubles)
        }
        for ch, i in line {
            if i > 0 {
                segment := line[i-1:i+1]
                if segment not_in doubles {
                    doubles[segment] = make([dynamic]int)
                }
                append(&doubles[segment], i)
            }
            if i > 1 {
                segment := line[i-2:i+1]
                if segment[0] == segment[2] {
                    triplets_check = true
                }
            }
        }
        doubles_check := false
        for key, value in doubles {
            if len(value) == 1 {
                continue
            }
            if key[0] == key[1] {
                check := false
                for i := 0; i < len(value); i += 1 {
                    for j := i + 1; j < len(value); j += 1 {
                        if math.abs(value[j] - value[i]) >= 2 {
                            check = true
                            break
                        }
                    }
                    if check {
                        break
                    }
                }
                if !check {
                    continue
                }
            }
            doubles_check = true
            break
        }
        if triplets_check && doubles_check {
            nice_count += 1
        }
    }
    return nice_count
}

main :: proc() {
    data := utils.get_data(#file)

    // p1
    tests := [?]TestCase{
        TestCase{"ugknbfddgicrmopn", 1},
        TestCase{"aaa", 1},
        TestCase{"jchzalrnumimnmhp", 0},
        TestCase{"haegwjzuvuyypxyu", 0},
        TestCase{"dvszwmarrgswjxmb", 0},
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
        TestCase{"qjhvhtzxzqqjkmpb", 1},
        TestCase{"xxyxx", 1},
        TestCase{"uurcxstgmygtbstg", 0},
        TestCase{"ieodomkazucvgmuy", 0},
        TestCase{"xyxy", 1},
        TestCase{"aabcbdefgaa", 1},
        TestCase{"hi12134567890hi", 1},
        TestCase{"aaa", 0},
        TestCase{"aaaa", 1},
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
