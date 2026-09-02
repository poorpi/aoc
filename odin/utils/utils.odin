package utils

import "core:os"
import "core:path/filepath"
import "core:fmt"

get_data :: proc(path : string, filename : string = "data.txt") -> string {
    dir := filepath.dir(path)
    datapath, error1 := filepath.join({dir, filename})
    if error1 != nil {
        return ""
    }
    data, error2 := os.read_entire_file(datapath, context.allocator)
    if error2 != nil {
        return ""
    }
    return string(data)
}