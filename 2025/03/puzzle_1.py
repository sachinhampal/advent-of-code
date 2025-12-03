import typing as _t


def calculate_power_output(banks: _t.Iterable[_t.Iterable[int]]) -> int:
    bank_iter = iter(banks)
    last_idx = len(list(next(bank_iter))) - 1
    total = 0
    for bank in banks:
        batteries_list = list(bank)
        max_num, max_idx = _get_max_and_idx(batteries_list)
        if max_idx == last_idx:
            second_num = max_num
            first_num, _ = _get_max_and_idx(batteries_list[:max_idx])
        else:
            first_num = max_num
            second_num, _ = _get_max_and_idx(batteries_list[max_idx + 1 :])

        total += (first_num * 10) + second_num

    return total


def _get_max_and_idx(numbers: _t.Iterable[int]) -> tuple[int, int]:
    max_num, max_idx = 1, 0
    for idx, num in enumerate(numbers):
        if num > max_num:
            max_num = num
            max_idx = idx

    return max_num, max_idx


def main(filepath) -> int:
    with open(filepath, encoding="utf-8") as f:
        banks_list = [[int(x) for x in y if x != "\n"] for y in f.readlines()]

    return calculate_power_output(banks_list)
