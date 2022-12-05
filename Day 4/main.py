from pprint import pp


DataType = list[tuple[tuple[int, int], tuple[int, int]]]
DataTypePart2 = list[str]

def range_contain_other(first_range: tuple[int, int], second_range: tuple[int, int]) -> bool:
    x_offset = first_range[0] - second_range[0]
    x1_offset = first_range[1] - second_range[1]
    if (x_offset >= 0 and x1_offset <= 0) or (x_offset <= 0 and x1_offset >= 0):
        return True
    return False

def range_overlap_other(first_range: tuple[int, int], second_range: tuple[int, int]) -> bool:
    x1, x2 = first_range
    y1, y2 = second_range
    return (y1 <= x1 and x1 <= y2) or \
        (y1 <= x2 and x2 <= y2) or \
        (x1 <= y1 and y1 <= x2) or \
        (x1 <= y2 and y2 <= x2)

def solution_part1(data: DataType) -> int:
    result = 0
    for x, y in data:
        if range_contain_other(x, y):
            result += 1
    return result

def solution_part2(data: DataTypePart2) -> int:
    result = 0
    for x, y in data:
        if range_overlap_other(x, y) or range_overlap_other(y, x):
            result += 1
    return result


def parce_input(file_name: str) -> DataType:
    with open(file_name, "r") as f:
        return list(map(lambda row: tuple(map(lambda x: tuple(map(int, x.split("-"))), row.strip().split(","))), f.readlines()))

if __name__ == '__main__':
    file_name = "input"
    data = parce_input(file_name)
    result = solution_part1(data)
    print(result)

    # data = parce_input_part2(file_name)
    result = solution_part2(data)
    print(result)
