import typing as _t


def get_max_and_idx(numbers: _t.Iterable[int]) -> tuple[int, int]:
    max_num, max_idx = 1, 0
    for idx, num in enumerate(numbers):
        if num > max_num:
            max_num = num
            max_idx = idx

    return max_num, max_idx


def main(filepath) -> int:
    with open(filepath, encoding="utf-8") as f:
        banks_iter = ([int(x) for x in y if x != "\n"] for y in f.read().splitlines())

    banks_list = list(banks_iter)
    last_idx = len(banks_list[0]) - 1
    total = 0
    for bank in banks_list:
        batteries_list = list(bank)
        max_num, max_idx = get_max_and_idx(batteries_list)
        if max_idx == last_idx:
            second_num = max_num
            first_num, _ = get_max_and_idx(batteries_list[:max_idx])
        else:
            first_num = max_num
            second_num, _ = get_max_and_idx(batteries_list[max_idx + 1 :])

        total += (first_num * 10) + second_num

    return total
