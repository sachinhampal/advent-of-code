import collections as _coll


def find_beam_split_count(
    starting_point: tuple[int, int], levels: list[list[str]]
) -> int:
    len_levels = len(levels)
    points_queue = _coll.deque([starting_point])
    split_count = 0
    while points_queue:
        row, col = points_queue.popleft()
        if levels[row][col] == "|":
            continue

        if levels[row][col] in {".", "S"}:
            levels[row][col] = "|"
            if (row + 1) < len_levels:
                points_queue.append((row + 1, col))

        else:
            split_count += 1
            levels[row][col - 1] = "|"
            levels[row][col + 1] = "|"
            points_queue.append((row + 1, col + 1))
            points_queue.append((row + 1, col - 1))

    return split_count


def main(filepath: str) -> int:
    with open(filepath) as f:
        row_iter = (row for row in f.read().splitlines())

    rows = [list(x) for x in row_iter]
    first_level = rows[0]
    starting_col_idx = 0
    for i, val in enumerate(first_level):
        if val == "S":
            starting_col_idx = i
            break

    return find_beam_split_count((0, starting_col_idx), rows)
