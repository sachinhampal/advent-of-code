def crack_code(
    rotations_list: list[str],
    *,
    max_dial_number: int = 100,
    starting_dial_number: int = 50,
) -> int:
    current_dial_number = starting_dial_number
    count = 0
    for rotation in rotations_list:
        direction, distance = rotation[0], int(rotation[1:])
        complete_rotations, remainder = divmod(distance, max_dial_number)
        count += complete_rotations
        multiplier = 1 if direction == "R" else -1
        new_dial_number = (
            current_dial_number + (remainder * multiplier)
        ) % max_dial_number
        add_extra_rotation = (
            (direction == "R" and new_dial_number < current_dial_number)
            or (direction == "L" and new_dial_number > current_dial_number)
        )
        
        # True condition resolve to `1` whereas false conditions resolve to `0`
        count += new_dial_number == 0 or (current_dial_number != 0 and add_extra_rotation)
        current_dial_number = new_dial_number

    return count


def main(file_path: str) -> int:
    with open(file_path) as f:
        rotations_list = f.readlines()
    return crack_code(rotations_list)


if __name__ == "__main__":
    main("input.txt")
