def crack_code(
    rotations_list: list[str],
    *,
    dial_limit: int = 100,
    starting_dial_number: int = 50,
) -> int:
    dial_number = starting_dial_number
    count = 0
    for rotation in rotations_list:
        direction, distance = rotation[0], int(rotation[1:])
        multiplier = 1 if direction == "R" else -1
        dial_number = (dial_number + (distance * multiplier)) % dial_limit

        # True conditions resolve to `1` whereas false conditions resolve to `0`
        count += dial_number == 0

    return count


def main(file_path: str) -> int:
    with open(file_path) as f:
        rotations_list = f.readlines()

    dial_limit = 100
    starting_dial_number = 50
    dial_number = starting_dial_number
    count = 0
    for rotation in rotations_list:
        direction, distance = rotation[0], int(rotation[1:])
        multiplier = 1 if direction == "R" else -1
        dial_number = (dial_number + (distance * multiplier)) % dial_limit

        # True conditions resolve to `1` whereas false conditions resolve to `0`
        count += dial_number == 0

    return count
