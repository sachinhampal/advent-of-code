def find_invalid_ids(id_ranges: list[str]) -> int:
    invalid_ids_total_sum = 0
    for id_range in id_ranges:
        start_str, end_str = id_range.split("-")
        start_int, end_int = int(start_str), int(end_str)
        for candidate_id in range(start_int, end_int + 1):
            candidate_id_str = str(candidate_id)
            len_candidate_id_str = len(candidate_id_str)
            if (candidate_id_str[0] == "0") or (len_candidate_id_str % 2 == 1):
                continue

            idx = len_candidate_id_str // 2
            if candidate_id_str[:idx] == candidate_id_str[idx:]:
                invalid_ids_total_sum += candidate_id

    return invalid_ids_total_sum


def main(filepath: str) -> int:
    with open(filepath, encoding="utf-8") as f:
        id_ranges = f.readlines()[0].split(",")

    return find_invalid_ids(id_ranges)
