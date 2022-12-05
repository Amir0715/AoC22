DataType = list[tuple[str, str]]
DataTypePart2 = list[str]

def solution_part1(data: DataType) -> int:
    result = 0
    for x, y in data:
        char = list(set(x).intersection(set(y)))[0]
        char_order = ord(char)
        if 97 <= char_order and char_order <= 122:
            result += char_order - 96
        elif 65 <= char_order and char_order <= 90:
            result += char_order - 38
    return result

def solution_part2(data: DataTypePart2) -> int:
    result = 0
    for x, y, z in zip(data[:-2:3], data[1:-1:3], data[2::3]):
        char = list(set(x).intersection(set(y)).intersection(set(z)))[0]
        char_order = ord(char)
        if 97 <= char_order and char_order <= 122:
            result += char_order - 96
        elif 65 <= char_order and char_order <= 90:
            result += char_order - 38
    return result


def parce_input(file_name: str) -> DataType:
    with open(file_name, "r") as f:
        return list(map(lambda x: tuple([x[i: i+len(x) // 2] for i in range(0, len(x), len(x) // 2)]), map(lambda x: x.strip(), f.readlines())))

def parce_input_part2(file_name: str) -> DataTypePart2:
    with open(file_name, "r") as f:
        return list(map(lambda x: x.strip(), f.readlines()))

if __name__ == '__main__':
    file_name = "input"
    data = parce_input(file_name)
    # print(data)
    result = solution_part1(data)
    print(result)

    data = parce_input_part2(file_name)
    result = solution_part2(data)
    print(result)
    # print(result)