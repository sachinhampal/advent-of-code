def get_number_of_papers_to_remove_2(papers_map: list[list[str]]):
    total = 0
    while True:
        count, coordinates_to_mark = get_number_of_papers_to_remove(papers_map)
        total += count
        if not coordinates_to_mark:
            break

        for x, y in coordinates_to_mark:
            papers_map[x][y] = "x"

    return total


def get_number_of_papers_to_remove(papers_map: list[list[str]]):
    max_row = len(papers_map[0])
    max_height = len(papers_map)

    count = 0
    coordinates_to_mark = []
    for y in range(max_height):
        for x in range(max_row):
            if papers_map[x][y] in {".", "x"}:
                continue

            if _get_neighboring_paper_count(papers_map, x, y, max_row, max_height) < 4:
                count += 1
                coordinates_to_mark.append((x, y))

    return count, coordinates_to_mark


def _get_neighboring_paper_count(papers_map, x, y, max_row, max_height):
    paper_count = 0
    for j in range(-1, 2):
        for i in range(-1, 2):
            if x == x + i and y == y + j:
                continue
            if x + i >= max_row or y + j >= max_height:
                continue
            if x + i < 0 or y + j < 0:
                continue

            item = papers_map[x + i][y + j]
            if item == "@":
                paper_count += 1

    return paper_count


def main(filepath: str):
    papers_map = []
    with open(filepath) as f:
        for row in f.readlines():
            papers_map.append([e for e in row if e != "\n"])

    return get_number_of_papers_to_remove_2(papers_map)
