import typing as _t


def calculate_power_output(banks: _t.Iterable[_t.Iterable[int]]) -> int:
    max_battery_number = 12
    bank_iter = iter(banks)
    len_bank = len(list(next(bank_iter)))
    total = 0
    for bank in banks:
        window = len_bank - max_battery_number + 1
        multiplier = max_battery_number - 1
        batteries_list = list(bank)
        sub_total = 0
        while multiplier >= 0:
            max_num, max_num_idx = get_max_and_idx(batteries_list[:window])
            sub_total += max_num * (10**multiplier)
            batteries_list = batteries_list[max_num_idx + 1 :]
            window -= max_num_idx
            multiplier -= 1

        total += sub_total

    return total


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

    max_battery_number = 12
    banks_list = list(banks_iter)
    len_bank = len(banks_list[0])
    total = 0
    for bank in banks_list:
        window = len_bank - max_battery_number + 1
        multiplier = max_battery_number - 1
        batteries_list = list(bank)
        sub_total = 0
        while multiplier >= 0:
            max_num, max_num_idx = get_max_and_idx(batteries_list[:window])
            sub_total += max_num * (10**multiplier)
            batteries_list = batteries_list[max_num_idx + 1 :]
            window -= max_num_idx
            multiplier -= 1

        total += sub_total

    return total
