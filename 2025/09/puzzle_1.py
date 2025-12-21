import itertools as _it


def main(filepath: str) -> int:
    with open(filepath, encoding="utf-8") as f:
        row_iter = (
            tuple([int(x) for x in row.split(",")]) for row in f.read().splitlines()
        )

    pairs_iter = iter(_it.combinations(row_iter, 2))
    largest_area = 0
    for pair in pairs_iter:
        a, b = pair
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        if area > largest_area:
            largest_area = area

    return largest_area
