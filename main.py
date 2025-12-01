import argparse as _ap
import importlib as _il


def main():
    parser = _ap.ArgumentParser()
    parser.add_argument("year", help="Edition of Advent Of Code to run.", type=int)
    parser.add_argument("day", help="Day number to run.", type=int)
    parser.add_argument("puzzle", help="Puzzle to run.", type=int)
    parser.add_argument(
        "--file_name",
        help="File name to run solution against. Optional, will default to 'input.txt'.",
    )
    args = parser.parse_args()
    year = args.year
    day = args.day
    puzzle = args.puzzle
    input_file_name = args.file_name or "input.txt"
    day_str = f"0{day}" if day < 10 else str(day)
    puzzle_path = f"{year}.{day_str}.puzzle_{puzzle}"
    mod = _il.import_module(puzzle_path)
    mod = _il.reload(mod)
    main_callable = getattr(mod, "main")
    input_data_file_path = f"{year}/{day_str}/{input_file_name}"
    answer = main_callable(input_data_file_path)
    print(f"Answer is: {answer}")


if __name__ == "__main__":
    main()
