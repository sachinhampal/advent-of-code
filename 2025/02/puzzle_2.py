import typing as _t


def find_invalid_ids(id_ranges: _t.Iterable[tuple[str, ...]]) -> int:
    invalid_ids_total_sum = 0
    for id_range in id_ranges:
        start_str, end_str = id_range
        start_int, end_int = int(start_str), int(end_str)
        for candidate_id in range(start_int, end_int + 1):
            candidate_id_str = str(candidate_id)
            len_candidate_id_str = len(candidate_id_str)
            if candidate_id_str[0] == "0":
                continue

            invalid_ids_found = set()
            for idx in range(1, len_candidate_id_str):
                candidate_sub_id = candidate_id_str[:idx]
                j = idx
                while j <= len_candidate_id_str:
                    nth_sub_id = candidate_id_str[j : j + idx]
                    if nth_sub_id == candidate_sub_id:
                        if (j + idx >= len_candidate_id_str) and (
                            candidate_id not in invalid_ids_found
                        ):
                            invalid_ids_total_sum += candidate_id
                            invalid_ids_found.add(candidate_id)
                            break

                        j += idx
                    else:
                        break

    return invalid_ids_total_sum


def main(filepath: str) -> int:
    with open(filepath, encoding="utf-8") as f:
        id_ranges = [tuple(x.split("-")) for x in f.readlines()[0].split(",")]

    return find_invalid_ids(id_ranges)
