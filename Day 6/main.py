from pprint import pp

DataType = str

def solution_part1(data: DataType):
    for start_window_index in range(4, len(data) - 3):
        window = data[start_window_index:start_window_index + 4]
        if len(set(window)) == 4:
            return start_window_index + 4

def solution_part2(data: DataType) -> int:
    for start_window_index in range(14, len(data) - 13):
        window = data[start_window_index:start_window_index + 14]
        if len(set(window)) == 14:
            return start_window_index + 14

def parce_input(file_name: str) -> DataType:
    with open(file_name, "r") as f:
        return f.readline().strip()

if __name__ == '__main__':
    file_name = "input"
    data = parce_input(file_name)
    # pp(data)
    result = solution_part1(data)
    print(result)
    result = solution_part2(data)
    print(result)
