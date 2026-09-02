package aoc

import "core:crypto/legacy/md5"
import "core:fmt"
import "core:strings"
import "core:strconv"
import "../../utils"

TestCase :: struct {
    data: string,
    result: int,
}

part_1 :: proc(data: string) -> int {
    n := 0
    buf : [64]u8
    for {
        copy(buf[:], data)
        num_str := strconv.write_int(buf[len(data):], i64(n), 10)
        input_len := len(data) + len(num_str)
        ctx: md5.Context
        md5.init(&ctx)
        md5.update(&ctx, buf[:input_len])
        hash: [16]u8
        md5.final(&ctx, hash[:])
        if hash[0] == 0 && hash[1] == 0 && (hash[2] & 0xF0) == 0 {
            return n
        }
        n += 1
    }
}

part_2 :: proc(data: string) -> int {
    n := 0
    buf : [64]u8
    for {
        copy(buf[:], data)
        num_str := strconv.write_int(buf[len(data):], i64(n), 10)
        input_len := len(data) + len(num_str)
        ctx: md5.Context
        md5.init(&ctx)
        md5.update(&ctx, buf[:input_len])
        hash: [16]u8
        md5.final(&ctx, hash[:])
        if hash[0] == 0 && hash[1] == 0 && hash[2] == 0 {
            return n
        }
        n += 1
    }
}

main :: proc() {
    data := utils.get_data(#file)

    // p1
    tests := [?]TestCase{

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
