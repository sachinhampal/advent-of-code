import functools as _ft
import operator as _op
import typing as _t


def solve_equations(
    operators: list[_t.Callable[..., int]], operands: list[list[int]]
) -> int:
    equations_len = len(operators)
    number_of_operands_per_equation = range(len(operands))
    running_total = 0
    for equation_idx in range(equations_len):
        nums = [operands[x][equation_idx] for x in number_of_operands_per_equation]
        operator = operators[equation_idx]
        total = _ft.reduce(operator, nums)
        running_total += total

    return running_total


def main(filepath: str) -> int:
    with open(filepath) as f:
        row_iter = (row for row in f.read().splitlines())

    operand_count = 4
    operands = [
        [int(x) for x in next(row_iter).strip().split()] for _ in range(operand_count)
    ]
    operator_map = {
        "+": _op.add,
        "*": _op.mul,
    }
    operators = [operator_map[x] for x in next(row_iter).strip().split()]

    return solve_equations(operators, operands)
