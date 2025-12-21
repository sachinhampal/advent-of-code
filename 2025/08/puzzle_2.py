import collections as _coll
import disjoint_set_union as _dsu
import math as _math


def compute_3d_euclidean_distance(p1: tuple[int, ...], p2: tuple[int, ...]) -> float:
    return _math.sqrt(
        (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
    )


def main(filepath: str) -> int:
    with open(filepath, encoding="utf-8") as f:
        row_list = [
            tuple([int(x) for x in row.split(",")]) for row in f.read().splitlines()
        ]

    len_row_list = len(row_list)
    idx_2_distance = {
        (i, j): compute_3d_euclidean_distance(row_i, row_j)
        for i, row_i in enumerate(row_list)
        for j, row_j in enumerate(row_list[i + 1 :], start=i + 1)
    }
    sorted_idx_distance = dict(sorted(idx_2_distance.items(), key=lambda item: item[1]))
    shortest_connections = list(sorted_idx_distance.keys())

    dsu = _dsu.DisjointSetUnion(len_row_list)
    for a, b in shortest_connections:
        dsu.union(a, b)
        roots = [dsu.find(i) for i in range(len_row_list)]
        if len((_coll.Counter(roots))) == 1:
            return row_list[a][0] * row_list[b][0]

    return -1
