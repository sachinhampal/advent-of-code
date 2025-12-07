import functools as _ft
import operator as _op


def main(filepath: str) -> int:
    # TODO: Revisit this solution
    with open(filepath) as f:
        row_iter = (row for row in f.read().splitlines())
        
    row_list = list(row_iter)
    operator_list = row_list[-1]
    len_operator_list = len(operator_list)
    ranges = []
    offset = 0
    operator_list = row_list[-1]
    for i in range(len_operator_list):
        if operator_list[i] in {"*", "+"}:
            count = 0
            j = i + 1
            while j < len(operator_list) and operator_list[j] not in {"*", "+"}:
                count += 1
                j += 1
            if j == len_operator_list:
                ranges.append((offset, len_operator_list))
            else:
                ranges.append((offset, i + count))
            offset = i + count + 1

    split_row_lists = [
        [row[r[0]: r[1]] for r in ranges] for row in row_list[:-1]
    ]
    stripped_operator_list = [operator_list[x] for x, _ in ranges]
    transposed_lists = list(zip(*split_row_lists))
    corrected_operands = [
        nums + (op,) for op, nums in zip(stripped_operator_list, transposed_lists)
    ]
    operator_map = {
        "+": _op.add,
        "*": _op.mul,
    }
    running_total = 0
    for k in range(len(corrected_operands) - 1, -1, -1):
        nums, operator_str = corrected_operands[k][:-1], corrected_operands[k][-1]
        max_len = len(nums[0])
        s = []
        for i in range(max_len-1, -1, -1):
            st = ""
            for j in range(len(nums)):
                st += nums[j][i]
            s.append(int(st))

        total = _ft.reduce(operator_map[operator_str], s)
        running_total += total

    return running_total