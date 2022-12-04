def solution_part1(data: list[list[int]]) -> int:
    return max(map(sum, data))

def solution_part2(data: list[list[int]]) -> int:
    return sum(sorted(map(sum, data), reverse=True)[:3])

def parce_input(file_name: str) -> list[list[int]]:
    data = []
    with open(file_name, "r") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        buf = []
        for line in lines:
            if line == "":
                data.append(buf)
                buf = []
                continue

            buf.append(int(line))
    return data

if __name__ == '__main__':
    file_name = "input"
    data = parce_input(file_name)
    result = solution_part1(data)
    print(result)
    result = solution_part2(data)
    print(result)