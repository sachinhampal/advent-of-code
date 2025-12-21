def main(file_path: str) -> int:
    with open(file_path) as f:
        rotations_list = f.readlines()

    dial_limit = 100
    starting_dial_number = 50
    current_dial_number = starting_dial_number
    count = 0
    for rotation in rotations_list:
        direction, distance = rotation[0], int(rotation[1:])
        complete_rotations, remainder = divmod(distance, dial_limit)
        count += complete_rotations
        multiplier = 1 if direction == "R" else -1
        new_dial_number = (current_dial_number + (remainder * multiplier)) % dial_limit
        add_extra_rotation = (
            direction == "R" and new_dial_number < current_dial_number
        ) or (direction == "L" and new_dial_number > current_dial_number)

        # True conditions resolve to `1` whereas false conditions resolve to `0`
        count += new_dial_number == 0 or (
            current_dial_number != 0 and add_extra_rotation
        )
        current_dial_number = new_dial_number

    return count
