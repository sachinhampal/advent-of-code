import shapely as _sh
import itertools as _it
import typing as _t


def get_rectangle(*args) -> _sh.Polygon:
    a, b = args
    x1, y1 = a
    x2, y2 = b
    c, d = (x1, y2), (x2, y1)
    return _sh.Polygon([a, c, b, d])


def main(filepath: str) -> int:
    with open(filepath, encoding="utf-8") as f:
        points_iter = (
            tuple([int(x) for x in row.split(",")]) for row in f.read().splitlines()
        )

    point_list: list[tuple[int, ...]] = list(points_iter)
    polygon = _sh.geometry.Polygon(point_list)
    pair_iter: _t.Iterable[tuple[tuple[int, ...], ...]] = _it.combinations(
        point_list, 2
    )
    largest_area = 0
    for pair in pair_iter:
        rectangle = get_rectangle(*pair)
        if polygon.covers(rectangle):
            a, b = pair
            area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            if area > largest_area:
                largest_area = area

    return largest_area
