

MOORE = [
    (-1,-1), (0,-1), (1,-1),
    (-1, 0),         (1, 0),
    (-1, 1), (0, 1), (1, 1)
]

VON_NEUMANN = [
            (0,-1),
    (-1,0),         (1,0),
            (0, 1)
]


def neighborhood(grid, x, y, offsets=None, wrap=False):
    offsets = offsets or MOORE
    h, w = len(grid), len(grid[0])
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if wrap:
            nx %= w
            ny %= h
        elif not (0 <= nx < w and 0 <= ny < h):
            continue
        yield grid[ny][nx]


def merge_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = []
    current_start, current_end = intervals[0]
    for start, end, *rest in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end, *rest))
            current_start = start
            current_end = end

    merged.append((current_start, current_end, *rest))
    return merged
