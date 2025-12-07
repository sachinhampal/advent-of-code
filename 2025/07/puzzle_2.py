import functools as _ft


@_ft.lru_cache
def find_beam_split_rec(
    point: tuple[int, int], len_levels: int, levels: tuple[tuple[int]]
) -> int:
    row_idx, col_idx = point
    if row_idx >= len_levels:
        return 1

    if levels[row_idx][col_idx] == ".":
        return find_beam_split_rec((row_idx + 1, col_idx), len_levels, levels)

    elif levels[row_idx][col_idx] == "^":
        return find_beam_split_rec(
            (row_idx, col_idx - 1), len_levels, levels
        ) + find_beam_split_rec((row_idx, col_idx + 1), len_levels, levels)

    return -1


def main(filepath: str) -> int:
    with open(filepath) as f:
        row_iter = (row for row in f.read().splitlines())

    rows = [list(x) for x in row_iter]
    starting_col = 0
    first_row = rows[0]
    for i, row_element in enumerate(first_row):
        if row_element == "S":
            starting_col = i
            break

    levels = tuple([tuple(row) for row in rows])
    len_levels = len(levels)
    return find_beam_split_rec((1, starting_col), len_levels, tuple(levels))
