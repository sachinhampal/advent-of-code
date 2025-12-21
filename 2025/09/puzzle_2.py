import itertools as _it
import numpy as _np
import typing as _t


def get_edges_list(
    point_list: list[tuple[int, ...]],
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    len_point_list = len(point_list)

    return [
        (point_list[i], point_list[(i + 1) % len_point_list])
        for i in range(len_point_list)
    ]


def get_rectangle_perimeter(points):
    perimeter = []
    for i in range(4):
        current_x, current_y = points[i]
        next_x, next_y = points[(i + 1) % 4]

        if next_x != current_x:
            step = 1 if next_x > current_x else -1
            for i in range(current_x, next_x, step):
                perimeter.append((i, current_y))

        elif next_y != current_y:
            step = 1 if next_y > current_y else -1
            for i in range(current_y, next_y, step):
                perimeter.append((current_x, i))

    return perimeter


def get_rectangle_points(a, b):
    """
    The alignment of the returned points are as follows:
    a         d
    +---------+
    |         |
    |         |
    |         |
    +---------+
    c         b
    """
    x1, y1 = a
    x2, y2 = b
    c, d = (x1, y2), (x2, y1)
    return a, c, b, d


def points_in_polygon(
    points: _t.Iterable[tuple[int, int]],
    edges: _t.Iterable[tuple[tuple[int, ...], ...]],
    tol=1e-10,
):
    """
    Check if points exist inside a polygon.
    An array consisting of `True` or `False` values is returned.
    `True` indicates the point exists on or in the polygon, and `False` if it doesnt.
    """
    points_array = _np.asarray(points)
    edges_array = _np.asarray(edges)

    p_x = points_array[:, 0][:, None]
    p_y = points_array[:, 1][:, None]

    a = edges_array[:, 0, :]
    b = edges_array[:, 1, :]

    a_x, a_y = a[:, 0], a[:, 1]
    b_x, b_y = b[:, 0], b[:, 1]

    ab_x = b_x - a_x
    ab_y = b_y - a_y

    ap_x = p_x - a_x
    ap_y = p_y - a_y

    cross = ab_x * ap_y - ab_y * ap_x
    dot = ap_x * ab_x + ap_y * ab_y
    len_sq = ab_x * ab_x + ab_y * ab_y

    on_edge = (_np.abs(cross) < tol) & (dot >= 0) & (dot <= len_sq)

    # If point lies on any edge we count it as inside the polygon
    on_edge_any = _np.any(on_edge, axis=1)

    # Ray cast algorithm
    # - Ensure a_y <= b_y
    swap = a_y > b_y
    a_x_s = _np.where(swap, b_x, a_x)
    b_x_s = _np.where(swap, a_x, b_x)
    a_y_s = _np.where(swap, b_y, a_y)
    b_y_s = _np.where(swap, a_y, b_y)

    y_in_bounds = (p_y >= a_y_s) & (p_y < b_y_s)
    not_too_far_right = p_x <= _np.maximum(a_x_s, b_x_s)
    potential = y_in_bounds & not_too_far_right

    left_of_both = p_x < _np.minimum(a_x_s, b_x_s)
    crossings = potential & left_of_both

    remaining = potential & ~left_of_both
    vertical = remaining & (a_x_s == b_x_s)
    crossings |= vertical & (p_x <= a_x_s)

    non_vertical = remaining & ~vertical
    if _np.any(non_vertical):
        x_intersection = a_x_s + (p_y - a_y_s) * (b_x_s - a_x_s) / (b_y_s - a_y_s)
        crossings |= non_vertical & (p_x <= x_intersection)

    inside = _np.sum(crossings, axis=1) % 2 == 1

    # Boundary overrides raycast
    return inside | on_edge_any


def main(filepath: str) -> int:
    with open(filepath, encoding="utf-8") as f:
        point_list = [
            tuple([int(x) for x in row.split(",")]) for row in f.read().splitlines()
        ]

    edges_tuple = tuple(get_edges_list(point_list))
    pairs_list = list(_it.combinations(point_list, 2))

    areas = {
        (a, b): (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1) for (a, b) in pairs_list
    }
    sorted_areas = dict(sorted(areas.items(), key=lambda item: item[1], reverse=True))
    for pair in sorted_areas:
        rectangle_points = get_rectangle_points(*pair)
        candidate_points = rectangle_points[1], rectangle_points[3]
        if not all(points_in_polygon(candidate_points, edges_tuple)):
            continue

        perimeter = get_rectangle_perimeter(rectangle_points)
        if all(points_in_polygon(perimeter, edges_tuple)):
            return sorted_areas[pair]

    return -1
